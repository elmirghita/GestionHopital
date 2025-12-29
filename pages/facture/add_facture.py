import streamlit as st
from pages.db import get_connection

def render_add_facture():
    st.header("➕ Ajouter une facture")

    with st.form("add_facture_form", clear_on_submit=True):

        avec_CNSS = st.checkbox("Avez-vous la CNSS ?")

        type_paiement = ["Espece", "Carte Bancaire", "Cheque"]
        mode_paiement = st.selectbox("Mode de paiement *", type_paiement)

        submitted = st.form_submit_button("Créer la facture", type="primary")

        if submitted:
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()

                    cursor.execute("""
                        INSERT INTO facture (avec_cnss, mode_paiement, montant_facture)
                        VALUES (%s, %s, 0)
                        RETURNING id_facture
                    """, (avec_CNSS, mode_paiement))

                    id_facture = cursor.fetchone()[0]
                    conn.commit()

                    st.success(f"✅ Facture créée avec succès (ID : {id_facture})")
                    st.info("➡️ Vous pouvez maintenant ajouter des lignes à cette facture")

            except Exception as e:
                st.error(f"❌ Erreur : {e}")

            finally:
                if conn:
                    conn.close()


