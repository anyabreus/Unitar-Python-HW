class RenovationCalculatorError(Exception):
    """Базова помилка."""


class DataFileError(RenovationCalculatorError):
    """Файл з даними не знайдено або його не можна прочитати."""


class InvalidRowError(RenovationCalculatorError):
    """Рядок даних має неправильний формат."""
