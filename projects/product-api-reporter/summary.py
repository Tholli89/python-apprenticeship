def summarize_products(products):
    total_products = 0
    total_price = 0
    highest_price = None
    lowest_price = None
    by_category = {}

    for product in products:
        price = product["price"]
        category = product["category"]

        total_products = total_products + 1
        total_price = total_price + price

        if highest_price is None or price > highest_price:
            highest_price = price

        if lowest_price is None or price < lowest_price:
            lowest_price = price

        by_category[category] = by_category.get(category, 0) + 1

    if total_products == 0:
        average_price = 0.0
    else:
        average_price = round(total_price / total_products, 2)

    return {
        "total_products": total_products,
        "average_price": average_price,
        "highest_price": highest_price,
        "lowest_price": lowest_price,
        "total_value": round(total_price, 2),
        "by_category": by_category,
    }