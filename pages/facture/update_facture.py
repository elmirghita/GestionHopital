import streamlit as st
from pages.db import get_connection

def render_update_facture():
    st.header("✏️ Modifier la facture")

    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_facture, montant_facture FROM facture
            ORDER BY date_facture;
        """)
        factures = cursor.fetchall()

        if not factures:
            st.info("ℹ️ Aucune facture trouve.")
            return

        facture_options = [f"(ID: {id}) {montant}DH" for id, montant in factures]
        selected = st.selectbox("Selectionnez une facture", facture_options)

        if selected:
            facture_id = int(selected.split(")")[0].replace("(ID: ", ""))

            cursor.execute("SELECT * FROM facture WHERE id_facture = %s", (facture_id,))
            current = cursor.fetchone()

            with st.form("update_form"):
                montant = st.number_input("Montant*", min_value = 0)
                avec_CNSS = st.checkbox("Avez-vous la CNSS ?")
                type_paiement = ["Espece", "Carte Bancaire", "Cheque"]
                
                mode_paiement = st.selectbox("Mode Paiement*", (type_paiement))
                submitted = st.form_submit_button("Mettre a jour", type="primary")

                if submitted:
                    cursor.execute("""
                        UPDATE facture SET montant_facture=%s, avec_cnss=%s,
                        mode_paiement=%s WHERE id_facture=%s""",
                        (montant, avec_CNSS, mode_paiement, facture_id))
                    
                    conn.commit()
                    st.success("✅ Facture mis a jour!")
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()