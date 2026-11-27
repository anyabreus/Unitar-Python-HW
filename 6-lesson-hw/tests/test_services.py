import pytest
from renovation_calculator.services import (
    calculate_category_cost,
    calculate_renovation_cost,
    calculate_square_m_cost,
    find_most_expensive_items,
)


def renovation_item(category, name, quantity, price):
    return {
        "category": category,
        "name": name,
        "quantity": quantity,
        "unit": "шт",
        "price": price,
    }


renovation_items = [
    renovation_item("Матеріали", "Фарба", 2, 210),
    renovation_item("Роботи", "Монтаж", 3, 500),
    renovation_item("Матеріали", "Клей", 4, 320),
]


def test_calculate_renovation_cost():
    assert calculate_renovation_cost(renovation_items) == 3200


def test_calculate_category_cost():
    assert calculate_category_cost(renovation_items, "Матеріали") == 1700
    assert calculate_category_cost(renovation_items, "Роботи") == 1500


def test_calculate_category_cost_rejects_unknown_category():
    with pytest.raises(ValueError):
        calculate_category_cost(renovation_items, "Інше")


def test_calculate_square_m_cost():
    assert calculate_square_m_cost(3190, 68) == 46.91


def test_calculate_square_m_cost_rejects_zero_apartment_size():
    with pytest.raises(ZeroDivisionError):
        calculate_square_m_cost(3190, 0)


def test_find_most_expensive_items_returns_three_items():
    expensive_items = find_most_expensive_items(renovation_items)

    assert [item["name"] for item in expensive_items] == ["Монтаж", "Клей", "Фарба"]
