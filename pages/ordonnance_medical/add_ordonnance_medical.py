import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_add_ordonnance_medical():
    st.subheader("➕ Ajouter un médicament à une ordonnance")

    conn = get_connection()

    ordonnances = pd.read_sql(
        "SELECT id_ordonnance, type_ordonnance FROM ordonnance",
        conn
    )

    medicaments = pd.read_sql(
        "SELECT id_medicament, nom_medicament FROM medicament",
        conn
    )

    conn.close()

    ordonnance_choice = st.selectbox(
        "Type d'ordonnance",
        ordonnances["type_ordonnance"]
    )

    medicament_choice = st.selectbox(
        "Nom du médicament",
        medicaments["nom_medicament"]
    )

    if st.button("Ajouter"):
        id_ord = ordonnances.loc[
            ordonnances["type_ordonnance"] == ordonnance_choice,
            "id_ordonnance"
        ].values[0]

        id_med = medicaments.loc[
            medicaments["nom_medicament"] == medicament_choice,
            "id_medicament"
        ].values[0]

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO ordonnance_medical (id_ordonnance, id_medicament)
            VALUES (%s, %s)
            """,
            (int(id_ord), int(id_med))
        )

        conn.commit()
        conn.close()

        st.success("Médicament ajouté avec succès ✅")
