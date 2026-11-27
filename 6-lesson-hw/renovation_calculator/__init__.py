"""Калькулятор ремонту квартири"""

__version__ = "1.0.0"

from .config import APARTMENT_SIZE, CATEGORIES, DATA_FILE
from .data_loader import load_data
from .exceptions import DataFileError
from .report import show_report
from .services import (
    calculate_category_cost,
    calculate_renovation_cost,
    calculate_square_m_cost,
    find_most_expensive_items,
)

__all__ = [
    "APARTMENT_SIZE",
    "CATEGORIES",
    "DATA_FILE",
    "DataFileError",
    "calculate_category_cost",
    "calculate_renovation_cost",
    "calculate_square_m_cost",
    "find_most_expensive_items",
    "load_data",
    "show_report",
]
