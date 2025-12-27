import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_display_admission():
    st.subheader("📋 Liste des admissions")

    conn = get_connection()
    if not conn:
        return

    try:
        query = """
            SELECT a.id_admission,
                   p.nom_patient || ' ' || p.prenom_patient AS patient,
                   s.num_salle,
                   s.type_chambre,
                   a.motif_admission
            FROM admission a
            JOIN patient p ON p.id_patient = a.id_patient
            JOIN salle_hospitalisation s ON s.id_salle_hospitalisation = a.id_salle_hospitalisation
            ORDER BY a.id_admission DESC
        """

        df = pd.read_sql(query, conn)
        st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
