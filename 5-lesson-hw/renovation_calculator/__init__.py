"""Калькулятор ремонту квартири"""

__version__ = "1.0.0"

from .config import APARTMENT_SIZE, DATA_FILE
from .data_loader import load_data
from .exceptions import DataFileError
from .report import format_report
from .services import (
    calculate_category_cost,
    calculate_renovation_cost,
    calculate_square_m_cost,
    find_most_expensive_items,
)

__all__ = [
    "APARTMENT_SIZE",
    "DATA_FILE",
    "DataFileError",
    "calculate_category_cost",
    "calculate_renovation_cost",
    "calculate_square_m_cost",
    "find_most_expensive_items",
    "format_report",
    "load_data",
]
