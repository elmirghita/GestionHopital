import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_display_salle():
    st.header("📋 Liste de tous les salles")

    col1, col2 = st.columns([1, 2])
    with col1:
        search = st.text_input("🔍 Rechercher (Num salle ou ID)", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["ID", "Num Salle", "Type Salle"])
    
    query = """
        SELECT * FROM salle_hospitalisation
    """

    # Search filter
    if search:
        query += f"""
            WHERE num_salle ILIKE '%{search}'
            OR id_salle_hospitalisation ILIKE '%{search}%'
        """

    # Sort the result
    if sort_by == 'ID':
        query += " ORDER BY id_salle_hospitalisation"
    elif sort_by == 'Num Salle':
        query += " ORDER BY num_salle"
    else:
        query += " ORDER BY type_chambre"
    
    conn = get_connection()
    
    if conn:
        try:
            # turns the table into a data frame
            df = pd.read_sql(query, conn)

            if not df.empty:
                st.metric("👥 Total Salles", len(df))

                # Display table
                st.dataframe(
                    df.rename(columns={
                        "id_salle_hospitalisation": "ID",
                        "num_salle": "Num Salle",
                        "type_chambre": "Type Salle"
                    }),
                    use_container_width = True
                )
            else:
                st.info("ℹ️ Aucune salle trouve.")
    
        except Exception as e:
            st.error(f"❌ Erreur: {e}")
        finally:
            conn.close()