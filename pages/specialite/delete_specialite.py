import streamlit as st
from pages.db import get_connection

def render_delete_specialite():
    st.subheader("🗑️ Supprimer une spécialité")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_specialite, type_specialite FROM specialite")
    specialites = cursor.fetchall()

    if not specialites:
        st.info("Aucune spécialité trouvée")
        return

    spec_dict = {s[1]: s[0] for s in specialites}

    selected = st.selectbox("Choisir une spécialité à supprimer", spec_dict.keys())

    if st.button("Supprimer"):
        try:
            # Vérifier si utilisée
            cursor.execute(
                "SELECT COUNT(*) FROM medecin WHERE id_specialite = %s",
                (spec_dict[selected],)
            )
            count = cursor.fetchone()[0]

            if count > 0:
                st.warning("⚠️ Cette spécialité est utilisée par des médecins")
            else:
                cursor.execute(
                    "DELETE FROM specialite WHERE id_specialite = %s",
                    (spec_dict[selected],)
                )
                conn.commit()
                st.success("✅ Spécialité supprimée")

        except Exception as e:
            st.error(f"❌ Erreur : {e}")
        finally:
            conn.close()
