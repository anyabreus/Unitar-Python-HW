from renovation_calculator import (
    APARTMENT_SIZE,
    DATA_FILE,
    DataFileError,
    calculate_category_cost,
    calculate_renovation_cost,
    calculate_square_m_cost,
    find_most_expensive_items,
    format_report,
    load_data,
)


def main():
    try:
        renovation_items, warnings = load_data(DATA_FILE)
        renovation_cost = calculate_renovation_cost(renovation_items)
        work_cost = calculate_category_cost(renovation_items, "Роботи")
        materials_cost = calculate_category_cost(renovation_items, "Матеріали")
        square_m_cost = calculate_square_m_cost(renovation_cost, APARTMENT_SIZE)
        most_expensive_items = find_most_expensive_items(renovation_items)

        print(
            format_report(
                len(renovation_items),
                renovation_cost,
                work_cost,
                materials_cost,
                most_expensive_items,
                square_m_cost,
                warnings,
            )
        )

    except DataFileError as error:
        print(f"Помилка з файлом з даними. {error}")
    except ZeroDivisionError as error:
        print(f"Помилка: {error}")
    except ValueError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()
