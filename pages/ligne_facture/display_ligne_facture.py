import streamlit as st
from pages.db import get_connection
import pandas as pd

def render_display_ligne_facture():
    st.header("📋 Lignes de facture")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_facture FROM facture ORDER BY id_facture DESC
    """)
    factures = cursor.fetchall()

    if not factures:
        st.warning("Aucune facture trouvée")
        return

    facture_id = st.selectbox(
        "Choisir une facture",
        [f[0] for f in factures]
    )

    cursor.execute("""
        SELECT 
            lf.id_ligne_facture,
            lf.montant,
            CASE 
                WHEN lf.id_consultation IS NOT NULL THEN 'Consultation'
                WHEN lf.id_admission IS NOT NULL THEN 'Admission'
            END AS type_ligne
        FROM ligne_facture lf
        WHERE lf.id_facture = %s
        ORDER BY lf.id_ligne_facture
    """, (facture_id,))

    rows = cursor.fetchall()

    if rows:
        df = pd.DataFrame(
            rows,
            columns=["ID Ligne", "Montant", "Type"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucune ligne pour cette facture")

    conn.close()
