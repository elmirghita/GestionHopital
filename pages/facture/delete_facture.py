import streamlit as st
from pages.db import get_connection

def render_delete_facture():
    st.header("🗑️ Supprimer une facture")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_facture, montant_facture FROM facture
            ORDER BY date_facture DESC
        """)
        factures = cursor.fetchall()

        if not factures:
            st.info("ℹ️ Aucune facture trouvée.")
            return

        facture_options = [
            f"(ID: {id_facture}) {montant} DH"
            for id_facture, montant in factures
        ]

        selected = st.selectbox("Sélectionnez une facture", facture_options)

        if selected:
            facture_id = int(selected.split(")")[0].replace("(ID: ", ""))

            confirm = st.checkbox("Je confirme la suppression")

            if confirm and st.button("Supprimer définitivement", type="secondary"):
                cursor.execute(
                    "DELETE FROM facture WHERE id_facture = %s",
                    (facture_id,)
                )
                conn.commit()

                st.success("✅ Facture supprimée avec succès")
                st.rerun()

    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()
