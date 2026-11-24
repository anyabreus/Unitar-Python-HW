from .services import get_item_cost


def format_report(
    items_len,
    renovation_cost,
    work_cost,
    materials_cost,
    most_expensive_items,
    square_m_cost,
    warnings,
):
    lines = [
        f"Кількість проаналізованих позицій: {items_len} ({len(warnings)} виключено через помилки (див. нижче))"
    ]

    lines.append(f"\nЗагальна вартість ремонту: {renovation_cost}.\n\tВ тому числі:")
    lines.append(f"\t- Вартість робіт: {work_cost}")
    lines.append(f"\t- Вартість матеріалів: {materials_cost}")

    lines.append("\nНайбільш дорогі позиції:")
    for item in most_expensive_items:
        lines.append(f"\t{item['name']} - Загальна вартість: {get_item_cost(item)}")

    lines.append(f"\nВартість ремонту за м²: {square_m_cost}")

    lines.append("\nПопередження:")
    for num, warning in enumerate(warnings, start=1):
        lines.append(f"\t{num}. {warning}")

    return "\n".join(lines)
