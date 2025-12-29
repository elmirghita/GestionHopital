import streamlit as st
from pages.db import get_connection
from utils.fk_helpers import get_or_create_id
import datetime

def render_add_ordonnance():
    st.header("➕ Ajouter une Ordonnance")

    with st.form("add_ordonnance_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            type_ordonnance = st.selectbox("Type d'ordonnance*",[
            "Ordonnance médicale",
            "Ordonnance d’examens",
            "Ordonnance de sortie"]
    )
        with col2:
            date_ordonnance = datetime.datetime.now()
            st.write(date_ordonnance.strftime("%d/%m/%Y %H:%M:%S"))
            notes = st.text_area("Notes de l'ordonnance",height=150,placeholder="Écris les notes ici...\n- Remarques"
)


        submitted = st.form_submit_button("Ajouter l'ordonnance",type="primary")

    
        if submitted:
            if type_ordonnance and date_ordonnance and notes:
                try:
                    conn = get_connection()
                    if conn:
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO ordonnance(date_ordonnance, remarques, type_ordonnance) VALUES (%s,%s,%s)",
                            (date_ordonnance, notes, type_ordonnance)
                        )
                        conn.commit()
                        st.success(f"✅ Ordonnance ajouté avec succès!")
                except Exception as e:
                    st.error(f"❌ Erreur: {e}")
                finally:
                    if conn:
                        conn.close()
            elif submitted:
                    st.warning("⚠️ Veuillez remplir toute les champs")

