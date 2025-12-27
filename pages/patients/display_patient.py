# pages/customers/display_customers.py
import streamlit as st
import pandas as pd
from pages.db import get_connection


def render_display_customers():
    """Render the 'Display Patients' tab"""
    st.header("📋 Liste de tous les patients")

    # Search and filter
    col1, col2 = st.columns([1, 2])
    with col1:
        search = st.text_input("🔍 Rechercher (Nom ou CIN)", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["Nom", "CIN", "ID"])

    # Base query
    query = """
        SELECT * FROM patient
    """

    # Search filter
    if search:
        query += f"""
            WHERE nom_patient ILIKE '%{search}%'
               OR cin_patient ILIKE '%{search}%'
        """

    # Sorting
    if sort_by == "Nom":
        query += " ORDER BY nom_patient"
    elif sort_by == "CIN":
        query += " ORDER BY cin_patient"
    else:
        query += " ORDER BY id_patient"

    # Execute query
    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)

            if not df.empty:
                # Metrics
                st.metric("👥 Total Patients", len(df))

                # Display table
                st.dataframe(
                    df.rename(columns={
                        "id_patient": "ID",
                        "nom_patient": "Nom",
                        "prenom_patient": "Prénom",
                        "tel_patient": "Téléphone",
                        "cin_patient": "CIN"
                    }),
                    use_container_width=True
                )
            else:
                st.info("ℹ️ Aucun patient trouvé.")

        except Exception as e:
            st.error(f"❌ Erreur: {e}")
        finally:
            conn.close()
