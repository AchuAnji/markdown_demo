import streamlit as st
import psycopg2
import pandas as pd
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

def get_recurring_defects():
    query = """
    SELECT
        dt.defect_name,
        COUNT(DISTINCT l.id) AS affected_lots
    FROM defect_occurrences d
    JOIN inspections i ON d.inspection_id = i.id
    JOIN lots l ON i.lot_id = l.id
    JOIN defect_types dt ON d.defect_type_id = dt.id
    WHERE d.quantity > 0
    GROUP BY dt.defect_name
    HAVING COUNT(DISTINCT l.id) > 1;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def get_one_off_defects():
    query = """
    SELECT
        dt.defect_name,
        COUNT(DISTINCT l.id) AS affected_lots
    FROM defect_occurrences d
    JOIN inspections i ON d.inspection_id = i.id
    JOIN lots l ON i.lot_id = l.id
    JOIN defect_types dt ON d.defect_type_id = dt.id
    WHERE d.quantity > 0
    GROUP BY dt.defect_name
    HAVING COUNT(DISTINCT l.id) = 1;
    """
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("Operations Defect Recurrence Dashboard")

recurring_df = get_recurring_defects()
one_off_df = get_one_off_defects()

st.header("Recurring Defects")

if recurring_df.empty:
    st.warning("No recurring defects found or insufficient data.")
else:
    st.dataframe(recurring_df)

st.header("One-Off Defects")

if one_off_df.empty:
    st.warning("No one-off defects found or insufficient data.")
else:
    st.dataframe(one_off_df)
