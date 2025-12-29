import streamlit as st
from pages.db import get_connection
from datetime import date, datetime


def render_display_consultation():
    st.header("📋 Liste des consultations")

    conn = get_connection()
    if not conn:
        st.error("Connexion impossible")
        return

    try:
        conn.rollback()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT c.id_consultation,
                   c.date_consultation,
                   c.heure,
                   p.nom_patient, p.prenom_patient,
                   m.nom_medecin, m.prenom_medecin,
                   o.type_ordonnance,
                   c.diagnostic
            FROM consultation c
            JOIN patient p ON c.id_patient = p.id_patient
            JOIN medecin m ON c.id_medecin = m.id_medecin
            JOIN ordonnance o ON c.id_ordonnance = o.id_ordonnance
            ORDER BY c.date_consultation DESC, c.heure DESC
        """)

        consultations = cursor.fetchall()

        if not consultations:
            st.info("ℹ️ Aucune consultation trouvée")
            return

        for c in consultations:
            st.markdown(f"""
            **🆔 Consultation :** {c[0]}  
            📅 **Date :** {c[1]} | ⏰ {c[2]}  
            🧑‍🦱 **Patient :** {c[3]} {c[4]}  
            👨‍⚕️ **Médecin :** {c[5]} {c[6]}  
            📄 **Type ordonnance :** {c[7]}  
            🩺 **Diagnostic :** {c[8]}
            ---
            """)

    except Exception as e:
        conn.rollback()
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
