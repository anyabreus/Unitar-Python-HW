import csv
from io import StringIO
from os import PathLike

from .config import CATEGORIES
from .exceptions import DataFileError, InvalidRowError


def parse_row(row):
    try:
        category = row["category"]
        name = row["name"]

        try:
            quantity = int(row["quantity"])
        except ValueError as error:
            raise InvalidRowError(
                f"Некоректна кількість ('quantity'): '{row['quantity']}'"
            ) from error

        try:
            price = float(row["price"])
        except ValueError as error:
            raise InvalidRowError(
                f"Некоректна ціна ('price'): '{row['price']}'"
            ) from error

    except KeyError as error:
        raise InvalidRowError(f"Немає стовпця '{error.args[0]}'") from error
    except ValueError as error:
        raise InvalidRowError(f"Некоректне значення: {error}") from error

    if category not in CATEGORIES:
        raise InvalidRowError(f"'category' має бути однією з: {', '.join(CATEGORIES)}")
    if name.strip() == "":
        raise InvalidRowError("Значення 'name' пусте")
    if quantity <= 0:
        raise InvalidRowError(
            "Значення 'quantity' не може бути від'ємним чи дорівнювати нулю"
        )
    if (
        price < 0
    ):  # нуль лишаємо, якщо, наприклад, хтось нам безкоштовно щось зробив чи віддав матеріал :)
        raise InvalidRowError("Значення 'price' не може бути від'ємним")

    return {
        "category": category,
        "name": name,
        "quantity": quantity,
        "unit": row["unit"],
        "price": price,
    }


def _read_rows(file):
    reader = csv.DictReader(file)
    renovation_items, warnings = [], []
    for line_number, row in enumerate(reader, start=2):
        try:
            renovation_items.append(parse_row(row))
        except InvalidRowError as error:
            warnings.append(f"Помилка у рядку {line_number}: {error}")
    return renovation_items, warnings


def load_data(source):
    try:
        if isinstance(source, (str, PathLike)):
            with open(source, encoding="utf-8-sig") as file:
                return _read_rows(file)

        content = source.getvalue().decode("utf-8-sig")
        return _read_rows(StringIO(content))
    except FileNotFoundError as error:
        raise DataFileError(f"Файл не знайдено: {source}") from error
    except PermissionError as error:
        raise DataFileError(f"Доступ до файлу {source} відхилено") from error
