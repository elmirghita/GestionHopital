import streamlit as st
from pages.db import get_connection

def render_update_ligne_facture():
    st.header("✏️ Modifier une ligne de facture")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_ligne_facture, montant
        FROM ligne_facture
        ORDER BY id_ligne_facture DESC
    """)
    lignes = cursor.fetchall()

    if not lignes:
        st.warning("Aucune ligne trouvée")
        return

    ligne_dict = {f"Ligne #{l[0]}": l for l in lignes}

    selected = st.selectbox(
        "Choisir une ligne",
        ligne_dict.keys()
    )

    id_ligne, old_montant = ligne_dict[selected]

    nouveau_montant = st.number_input(
        "Nouveau montant",
        min_value=0.0,
        value=float(old_montant)
    )

    if st.button("Mettre à jour", type="primary"):
        try:
            cursor.execute("""
                UPDATE ligne_facture
                SET montant = %s
                WHERE id_ligne_facture = %s
            """, (nouveau_montant, id_ligne))

            cursor.execute("""
                UPDATE facture
                SET montant_facture = (
                    SELECT COALESCE(SUM(montant), 0)
                    FROM ligne_facture
                    WHERE id_facture = (
                        SELECT id_facture FROM ligne_facture WHERE id_ligne_facture = %s
                    )
                )
                WHERE id_facture = (
                    SELECT id_facture FROM ligne_facture WHERE id_ligne_facture = %s
                )
            """, (id_ligne, id_ligne))

            conn.commit()
            st.success("✅ Ligne mise à jour")

        except Exception as e:
            conn.rollback()
            st.error(e)

    conn.close()
