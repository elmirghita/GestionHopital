import streamlit as st
import pandas as pd
from pages.db import get_connection

def render_display_facture():
    st.header("📋 Liste de tous les factures")

    col1, col2 = st.columns([1, 2])
    with col1:
        search = st.text_input("🔍 Rechercher (Date ou Montant)", "")
    with col2:
        sort_by = st.selectbox("Trier par", ["Montant", "Date", "ID"])
    
    query = """
        SELECT * FROM facture
    """

    if search:
        query += f"""
            WHERE CAST(date_facture AS TEXT) ILIKE '%{search}%'
            OR CAST(montant_facture AS TEXT) ILIKE '%{search}%'
        """

    if sort_by == "Montant":
        query += " ORDER BY montant_facture"
    elif sort_by == "Date":
        query += " ORDER BY date_facture"
    else:
        query += " ORDER BY id_facture"

    conn = get_connection()
    if conn:
        try:
            df = pd.read_sql(query, conn)

            if not df.empty:

                col1, col2 = st.columns([1, 2])
                with col1:
                    st.metric("💵 Total des Factures", len(df))
                with col2:
                    st.metric("💰 Montant Total", f"{df['montant_facture'].sum():,.2f}DH")


                st.dataframe(
                    df.rename(columns= {
                        "id_facture": "ID",
                        "montant_facture": "Montant",
                        "date_facture": "Date",
                        "avec_cnss": "avec_CNSS",
                        "mode_paiement": "Mode Paiement"
                    }),
                    use_container_width = True
                )
            else:
                st.info("ℹ️ Aucune facture trouve.")
        
        except Exception as e:
            st.error(f"❌ Erreur: {e}")
        finally:
            conn.close()