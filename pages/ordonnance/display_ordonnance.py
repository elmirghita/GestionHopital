# pages/ordonnances/display_ordonnances.py
import streamlit as st
import pandas as pd
from pages.db import get_connection


def render_display_ordonnance():
    """Render the 'Display ordonnances' tab"""
    st.header("📋 Liste de tous les ordonnances")

    # Search and filter
    col1, col2 = st.columns([1, 2])
    with col1:
        search = st.text_input("🔍 Rechercher (Type ou ID)", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["Type", "ID"])

    # Base query
    query = """
        SELECT * FROM ordonnance
    """

    # Search filter
    if search:
        query += f"""
            WHERE type_ordonnance ILIKE '%{search}%'
               OR id_ordonnance ILIKE '%{search}%'
        """

    # Sorting
    if sort_by == "Type":
        query += " ORDER BY type_ordonnance"
    else:
        query += " ORDER BY id_ordonnance"

    # Execute query
    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)

            if not df.empty:
                # Metrics
                st.metric("👥 Total ordonnances", len(df))

                # Display table
                st.dataframe(
                    df.rename(columns={
                        "id_ordonnance": "ID",
                        "type_ordonnance": "Type",
                        "date_ordonnance": "Date",
                        "remarques": "Notes",
                    }),
                    use_container_width=True
                )
            else:
                st.info("ℹ️ Aucun ordonnance trouvé.")

        except Exception as e:
            st.error(f"❌ Erreur: {e}")
        finally:
            conn.close()
