from .config import CATEGORIES


def calculate_renovation_cost(renovation_items):
    return sum(
        (renovation_item["price"] * renovation_item["quantity"])
        for renovation_item in renovation_items
    )


def calculate_category_cost(renovation_items, category):
    if category not in CATEGORIES:
        raise ValueError(
            f"У розрахунку вартості по категорії значення 'category' має бути однією з: {', '.join(CATEGORIES)}"
        )
    return sum(
        (renovation_item["price"] * renovation_item["quantity"])
        for renovation_item in renovation_items
        if renovation_item["category"] == category
    )


def calculate_square_m_cost(renovation_cost, apartment_size):
    if apartment_size == 0:
        raise ZeroDivisionError("На нуль ділити не можна (розрахунок вартості м²)")
    return round(renovation_cost / apartment_size, 2)


def get_item_cost(renovation_item):
    return renovation_item["price"] * renovation_item["quantity"]


def find_most_expensive_items(renovation_items):
    return sorted(renovation_items, key=get_item_cost, reverse=True)[:3]
