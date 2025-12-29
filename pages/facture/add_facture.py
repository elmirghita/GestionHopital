import streamlit as st
from pages.db import get_connection
from datetime import date

def render_add_facture():
    st.header("➕ Ajouter une facture")

    with st.form("add_facture_form", clear_on_submit=True):

        montant = st.number_input("Montant*", min_value = 0)
        avec_CNSS = st.checkbox("Avez-vous la CNSS ?")
        type_paiement = ["Espece", "Carte Bancaire", "Cheque"]
        
        mode_paiement = st.selectbox("Mode Paiement*", (type_paiement))
        submitted = st.form_submit_button("Ajouter la facture", type="primary")

        if submitted and montant and type_paiement:
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO facture (montant_facture, avec_cnss, mode_paiement)
                        VALUES (%s, %s, %s)""",
                        (montant, avec_CNSS, mode_paiement))
                    
                    conn.commit()
                    st.success(f"✅ Facture du montant {montant} ajoute avec succes")
            except Exception as e:
                st.error(f"❌ Erreur: {e}")
            finally:
                if conn:
                    conn.close()
        elif submitted:
            st.warning("⚠️ Veuillez remplir tout les champs")


