import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_display_medicament():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM medicament", conn)
    conn.close()
    st.dataframe(df)
