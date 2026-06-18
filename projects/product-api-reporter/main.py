import requests
from summary import summarize_products


API_URL = "https://fakestoreapi.com/products"


def fetch_products():
    response = requests.get(API_URL, timeout=10)

    response.raise_for_status()  # will raise an error if status is 4xx/5xx [web:453][web:462]

    data = response.json()  # list of product dicts from the API [web:453][web:454][web:446]

    products = []
    for item in data:
        products.append(
            {
                "title": item["title"],
                "price": float(item["price"]),
                "category": item["category"],
            }
        )

    return products


def print_report(summary):
    print(f"Total products   : {summary['total_products']}")
    print(f"Average price    : {summary['average_price']}")
    print(f"Highest price    : {summary['highest_price']}")
    print(f"Lowest price     : {summary['lowest_price']}")
    print(f"Total value      : {summary['total_value']}")
    print(f"By category      : {summary['by_category']}")


def main():
    products = fetch_products()
    summary = summarize_products(products)
    print_report(summary)


if __name__ == "__main__":
    main()