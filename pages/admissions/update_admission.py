import streamlit as st
from pages.db import get_connection

def render_update_admission():
    st.subheader("✏️ Modifier une admission")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.id_admission,
                   p.nom_patient,
                   p.prenom_patient,
                   s.num_salle
            FROM admission a
            JOIN patient p ON p.id_patient = a.id_patient
            JOIN salle_hospitalisation s ON s.id_salle_hospitalisation = a.id_salle_hospitalisation
            ORDER BY a.id_admission
        """)
        admissions = cursor.fetchall()

        if not admissions:
            st.info("Aucune admission trouvée")
            return

        admission_options = {
            f"Admission {id} - {nom} {prenom} (Salle {salle})": id
            for id, nom, prenom, salle in admissions
        }

        selected = st.selectbox(
            "Sélectionner une admission",
            admission_options.keys()
        )
        id_admission = admission_options[selected]

        # Nouvelle salle
        cursor.execute("""
            SELECT * FROM salle_hospitalisation
        """)
        salles = cursor.fetchall()

        salle_options = {
            f"Salle {num} - {type_}": id_salle
            for id_salle, num, type_ in salles
        }

        new_salle = st.selectbox(
            "Nouvelle salle",
            salle_options.keys()
        )
        id_salle = salle_options[new_salle]

        new_motif = st.text_area("Nouveau motif")

        if st.button("💾 Mettre à jour"):
            cursor.execute("""
                UPDATE admission
                SET id_salle_hospitalisation = %s,
                    motif_admission = %s
                WHERE id_admission = %s
            """, (id_salle, new_motif, id_admission))

            conn.commit()
            st.success("✅ Admission mise à jour")

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
