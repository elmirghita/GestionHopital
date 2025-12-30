import streamlit as st
from pages.db import get_connection

def render_add_ligne_facture():
    st.subheader("➕ Nouvelle ligne facture")

    conn = get_connection()
    if not conn:
        return
    
    cursor = conn.cursor()

    cursor.execute("""SELECT id_facture FROM facture""")
    factures = cursor.fetchall()

    if not factures:
        st.warning("⚠️ Aucune facture trouvée")
        conn.close()
        return
    
    facture_dict = {f"Facture #{f[0]}": f[0] for f in factures}


    type_ligne = st.selectbox(
        "Type de ligne*",
        ["Consultation", "Admission"]
    )


    with st.form("add_ligne_facture_form"):
        facture_label = st.selectbox("Facture *", list(facture_dict.keys()))
        id_facture = facture_dict[facture_label]

        montant = st.number_input("Montant*", min_value=0.0, format="%.2f")

        id_consultation = None
        id_admission = None

        if type_ligne == "Consultation":

            cursor.execute("""
                SELECT c.id_consultation, p.nom_patient, p.prenom_patient, c.date_consultation 
                FROM consultation c
                JOIN patient p ON c.id_patient = p.id_patient
            """)
            consultations = cursor.fetchall()
            
            if consultations:
                options = {f"ID {c[0]} - {c[1]} {c[2]} ({c[3]})": c[0] for c in consultations}
                consultation_label = st.selectbox("Sélectionnez la Consultation *", list(options.keys()))
                id_consultation = options[consultation_label]
            else:
                st.info("Aucune consultation enregistrée.")

        elif type_ligne == "Admission":

            cursor.execute("""
                SELECT a.id_admission, p.nom_patient, p.prenom_patient
                FROM admission a
                JOIN patient p ON a.id_patient = p.id_patient
            """)
            admissions = cursor.fetchall()
            
            if admissions:
                options = {f"ID {a[0]} - {a[1]} {a[2]}": a[0] for a in admissions}
                admission_label = st.selectbox("Sélectionnez l'Admission *", list(options.keys()))
                id_admission = options[admission_label]
            else:
                st.info("Aucune admission enregistrée.")

        submitted = st.form_submit_button("Ajouter la ligne", type="primary")

        if submitted:

            is_valid = (type_ligne == "Consultation" and id_consultation) or \
                       (type_ligne == "Admission" and id_admission)

            if not is_valid:
                st.error(f"Veuillez sélectionner une {type_ligne.lower()}.")
            elif montant <= 0:
                st.error("Le montant doit être supérieur à 0.")
            else:
                try:
                    # Insertion de la ligne (l'autre ID restera NULL)
                    cursor.execute("""
                        INSERT INTO ligne_facture (id_facture, id_consultation, id_admission, montant)
                        VALUES (%s, %s, %s, %s)
                    """, (id_facture, id_consultation, id_admission, montant))

                    # Mise à jour automatique du montant total dans la table 'facture'
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
                    st.success("✅ Ligne ajoutée et total facture mis à jour !")


                except Exception as e:
                    conn.rollback()
                    st.error(f"❌ Erreur lors de l'insertion : {e}")

    cursor.close()
    conn.close()