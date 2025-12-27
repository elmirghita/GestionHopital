import streamlit as st
from pages.db import get_connection

def render_delete_departement():
    st.subheader("🗑️ Supprimer un département")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_departement, nom_departement FROM departement")
    departements = cursor.fetchall()

    if not departements:
        st.info("Aucun département trouvé")
        return

    dep_dict = {d[1]: d[0] for d in departements}

    selected = st.selectbox("Choisir un département à supprimer", dep_dict.keys())

    if st.button("Supprimer"):
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM medecin WHERE id_departement = %s",
                (dep_dict[selected],)
            )
            count = cursor.fetchone()[0]

            if count > 0:
                st.warning("⚠️ Ce département est utilisé par des médecins")
            else:
                cursor.execute(
                    "DELETE FROM departement WHERE id_departement = %s",
                    (dep_dict[selected],)
                )
                conn.commit()
                st.success("✅ Département supprimé")

        except Exception as e:
            st.error(f"❌ Erreur : {e}")
        finally:
            conn.close()
