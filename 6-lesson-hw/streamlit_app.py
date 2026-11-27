import streamlit as st
from renovation_calculator import (
    APARTMENT_SIZE,
    CATEGORIES,
    DATA_FILE,
    DataFileError,
    calculate_category_cost,
    calculate_renovation_cost,
    calculate_square_m_cost,
    find_most_expensive_items,
    load_data,
    show_report,
)

st.set_page_config(page_title="Калькулятор ремонту", layout="wide")
st.title("Скільки коштує ремонт?")
st.caption(
    'Порахуй, скільки коштує твій ремонт за м² та які позиції "тягнуть" найбільше з твого бюджету'
)

uploaded = st.sidebar.file_uploader("CSV файл з витратами на ремонт", type="csv")

apart_size = st.sidebar.number_input(
    label="Метраж квартири, м²",
    value=APARTMENT_SIZE,
    min_value=10.00,
    format="%.2f",
    required=True,
)
category = st.sidebar.selectbox("Категорія", ["Всі", *CATEGORIES])

try:
    if uploaded is None:
        st.info(
            "Показано приклад data/renovation.csv. Завантаж свій файл, щоб розрахувати показники по ньому"
        )
    renovation_items, warnings = load_data(uploaded or DATA_FILE)

    report_items = (
        renovation_items
        if category == "Всі"
        else [item for item in renovation_items if item["category"] == category]
    )
    renovation_cost = calculate_renovation_cost(report_items)
    categories_cost = {}
    for cat in CATEGORIES:
        categories_cost[cat] = calculate_category_cost(renovation_items, cat)
    square_m_cost = calculate_square_m_cost(renovation_cost, apart_size)
    most_expensive_items = find_most_expensive_items(report_items)

    show_report(
        len(report_items),
        category,
        categories_cost,
        renovation_cost,
        most_expensive_items,
        square_m_cost,
        warnings,
    )
except DataFileError as error:
    st.error(f"Помилка з файлом з даними. {error}")
except ZeroDivisionError as error:
    st.error(f"Помилка: {error}")
except ValueError as error:
    st.error(f"Помилка: {error}")
