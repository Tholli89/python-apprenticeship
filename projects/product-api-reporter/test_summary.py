import summary


def test_mixed_categories():
    products = [
        {"title": "Bag", "price": 39.99, "category": "accessories"},
        {"title": "Shirt", "price": 19.99, "category": "clothing"},
        {"title": "Hat", "price": 14.99, "category": "clothing"},
    ]

    result = summary.summarize_products(products)

    assert result["total_products"] == 3
    assert result["average_price"] == 24.99
    assert result["highest_price"] == 39.99
    assert result["lowest_price"] == 14.99
    assert result["total_value"] == 74.97
    assert result["by_category"] == {"accessories": 1, "clothing": 2}


def test_single_category():
    products = [
        {"title": "Phone", "price": 199.99, "category": "electronics"},
        {"title": "Headphones", "price": 89.99, "category": "electronics"},
    ]

    result = summary.summarize_products(products)

    assert result["total_products"] == 2
    assert result["average_price"] == 144.99
    assert result["highest_price"] == 199.99
    assert result["lowest_price"] == 89.99
    assert result["total_value"] == 289.98
    assert result["by_category"] == {"electronics": 2}


def test_empty_products():
    products = []

    result = summary.summarize_products(products)

    assert result["total_products"] == 0
    assert result["average_price"] == 0.0
    assert result["highest_price"] is None
    assert result["lowest_price"] is None
    assert result["total_value"] == 0
    assert result["by_category"] == {}