import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_display_ordonnance_medical():
    conn = get_connection()
    query = """
    SELECT 
        o.type_ordonnance,
        m.nom_medicament
    FROM ordonnance_medical om
    JOIN ordonnance o ON om.id_ordonnance = o.id_ordonnance
    JOIN medicament m ON om.id_medicament = m.id_medicament
    """
    df = pd.read_sql(query, conn)
    conn.close()
    st.dataframe(df)
