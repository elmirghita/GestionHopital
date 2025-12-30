import streamlit as st
from pages.db import get_connection

def render_delete_ligne_facture():
    st.subheader("🗑️ Supprimer une ligne de facture")

    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor()

    cursor.execute("""
        SELECT lf.id_ligne_facture, lf.id_facture, lf.montant, 
        p.nom_patient, p.prenom_patient
        FROM ligne_facture lf
        JOIN facture f ON id_ligne_facture = f.id_facture
        LEFT JOIN consultation c ON lf.id_consultation = c.id_consultation
        LEFT JOIN admission a ON lf.id_admission = a.id_admission
        LEFT JOIN patient p ON (c.id_patient = p.id_patient OR a.id_patient = p.id_patient)
        ORDER BY lf.id_ligne_facture DESC
    """)
    lignes_factures = cursor.fetchall()

    if not lignes_factures:
        st.warning("⚠️ Aucune ligne de facture trouvée.")
        conn.close()
        return
    
    ligne_options = {}
    for l in lignes_factures:
        label = f"Ligne #{l[0]} | Facture #{l[1]} | Patient: {l[3]} {l[4]} | {l[2]} DH"
        ligne_options[label] = (l[0], l[1]) 

    selected_label = st.selectbox("Choisir la ligne à supprimer :", list(ligne_options.keys()))
    id_ligne, id_facture = ligne_options[selected_label]


    if st.button("Confirmer la suppression", type="primary"):
        try:

            cursor.execute("""
                DELETE FROM ligne_facture 
                WHERE id_ligne_facture = %s
            """, (id_ligne,))


            cursor.execute("""
                UPDATE facture 
                SET montant_facture = (
                    SELECT COALESCE(SUM(montant), 0) 
                    FROM ligne_facture 
                    WHERE id_facture = %s
                ) 
                WHERE id_facture = %s
            """, (id_facture, id_facture))

            conn.commit()
            st.success(f"✅ La ligne #{id_ligne} a été supprimée et la facture #{id_facture} mise à jour.")
            
            st.rerun()

        except Exception as e:
            conn.rollback()
            st.error(f"❌ Erreur lors de la suppression : {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        st.info("Cliquez sur le bouton rouge pour valider la suppression définitive.")