import streamlit as st
from pages.db import get_connection

def render_delete_admission():
    st.subheader("🗑️ Supprimer une admission")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                admission.id_admission,
                patient.nom_patient,
                patient.prenom_patient,
                admission.id_salle_hospitalisation
            FROM admission
            JOIN patient 
                ON admission.id_patient = patient.id_patient
            ORDER BY admission.id_admission DESC
        """)

        admissions = cursor.fetchall()

        if not admissions:
            st.info("ℹ️ Aucune admission trouvée")
            return

        admission_options = {
            f"Admission {id_adm} | {nom} {prenom} | Salle {num_salle}": id_adm
            for id_adm, nom, prenom, num_salle in admissions
        }

        selected_label = st.selectbox(
            "Sélectionnez une admission",
            list(admission_options.keys())
        )

        id_admission = admission_options[selected_label]

        st.warning("⚠️ Cette action est irréversible")

        if st.checkbox("Je confirme la suppression"):
            if st.button("Supprimer définitivement", type="secondary"):
                cursor.execute(
                    "DELETE FROM admission WHERE id_admission = %s",
                    (id_admission,)
                )
                conn.commit()

                st.success("✅ Admission supprimée avec succès")
                st.rerun()

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
