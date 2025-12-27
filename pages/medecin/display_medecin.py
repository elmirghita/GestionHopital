# pages/medecins/display_medecins.py
import streamlit as st
import pandas as pd
from pages.db import get_connection


def render_display_medecin():
    """Render the 'Display medecins' tab"""
    st.header("📋 Liste de tous les medecins")

    # Search and filter
    col1, col2 = st.columns([1, 2])
    with col1:
        search = st.text_input("🔍 Rechercher (Nom ou ID)", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["Nom", "ID"])

    # Base query
    query = """
        SELECT * FROM medecin
    """

    # Search filter
    if search:
        query += f"""
            WHERE nom_medecin ILIKE '%{search}%'
               OR cin_medecin ILIKE '%{search}%'
        """

    # Sorting
    if sort_by == "Nom":
        query += " ORDER BY nom_medecin"
    else:
        query += " ORDER BY id_medecin"

    # Execute query
    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)

            if not df.empty:
                # Metrics
                st.metric("👥 Total medecins", len(df))

                # Display table
                st.dataframe(
                    df.rename(columns={
                        "id_medecin": "ID",
                        "nom_medecin": "Nom",
                        "prenom_medecin": "Prénom",
                        "tel_medecin": "Téléphone",
                        "type_specialite": "Specialite",
                        "nom_departement":"Departement"
                    
                    }),
                    use_container_width=True
                )
            else:
                st.info("ℹ️ Aucun medecin trouvé.")

        except Exception as e:
            st.error(f"❌ Erreur: {e}")
        finally:
            conn.close()
