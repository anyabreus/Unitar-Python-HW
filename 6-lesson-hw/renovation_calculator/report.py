import streamlit as st

from .config import CATEGORIES
from .services import get_item_cost


def format_cost(cost):
    return f"{cost:,.2f}".replace(",", " ").replace(".", ",") + " грн"


def show_report(
    items_len,
    curr_category,
    categories_cost,
    renovation_cost,
    most_expensive_items,
    square_m_cost,
    warnings,
):
    st.markdown(
        f"**Кількість проаналізованих позицій:** {items_len}"
        + (
            f" ({len(warnings)} виключено через помилки (див. нижче))"
            if warnings
            else ""
        )
    )

    is_all = curr_category == "Всі"
    all_category_text = f' (по категорії "{curr_category}")' if not is_all else ""

    if items_len != 0:
        left, right = st.columns(2)
        left.metric(
            f"Загальна вартість ремонту{all_category_text}",
            format_cost(renovation_cost),
            border=True,
        )
        right.metric(
            f"Вартість ремонту за м²{all_category_text}",
            format_cost(square_m_cost),
            border=True,
        )

        if is_all:
            st.subheader("Витрати за категоріями")
            cols = st.columns(len(CATEGORIES))
            for i, cat in enumerate(CATEGORIES):
                cols[i].metric(
                    f"**{cat}**", format_cost(categories_cost[cat]), border=True
                )

        st.divider()
        st.subheader("Найбільш дорогі позиції")
        most_expensive_lines = []
        for item in most_expensive_items:
            most_expensive_lines.append(
                f"- *{item['name']}*: {format_cost(get_item_cost(item))}"
            )
        st.markdown("\n".join(most_expensive_lines))
    else:
        st.info("Немає валідних даних для розрахунку")

    if len(warnings) != 0:
        st.warning("**Попередження:**")
        for num, warning in enumerate(warnings, start=1):
            st.markdown(f"\t{num}. {warning}")
