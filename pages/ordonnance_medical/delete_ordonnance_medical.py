import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_delete_ordonnance_medical():
    st.subheader("🗑 Supprimer un médicament d'une ordonnance")

    conn = get_connection()
    df = pd.read_sql("""
        SELECT 
            om.id_ordonnance,
            om.id_medicament,
            o.type_ordonnance,
            m.nom_medicament
        FROM ordonnance_medical om
        JOIN ordonnance o ON om.id_ordonnance = o.id_ordonnance
        JOIN medicament m ON om.id_medicament = m.id_medicament
    """, conn)
    conn.close()

    if df.empty:
        st.info("Aucune association trouvée")
        return

    choice = st.selectbox(
        "Sélectionner l'association",
        df.index,
        format_func=lambda i: f"{df.loc[i,'type_ordonnance']} → {df.loc[i,'nom_medicament']}"
    )

    if st.button("Supprimer"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            DELETE FROM ordonnance_medical
            WHERE id_ordonnance = %s AND id_medicament = %s
            """,
            (
                int(df.loc[choice, "id_ordonnance"]),
                int(df.loc[choice, "id_medicament"])
            )
        )

        conn.commit()
        conn.close()

        st.success("Suppression réussie 🗑")
