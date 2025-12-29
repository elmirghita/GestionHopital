import streamlit as st
from pages.db import get_connection

def render_delete_medicament():
    st.subheader("🗑️ Supprimer un medicament")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_medicament, nom_medicament FROM medicament")
    medicaments = cursor.fetchall()

    if not medicaments:
        st.info("Aucun medicament trouvé")
        return

    dep_dict = {d[1]: d[0] for d in medicaments}

    selected = st.selectbox("Choisir un medicament à supprimer", dep_dict.keys())

    if st.button("Supprimer"):
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM medicament WHERE id_medicament = %s",
                (dep_dict[selected],)
            )
            count = cursor.fetchone()[0]

            if count > 0:
                st.warning("⚠️ Ce medicament est utilisé dans des ordonnances")
            else:
                cursor.execute(
                    "DELETE FROM medicament WHERE id_medicament = %s",
                    (dep_dict[selected],)
                )
                conn.commit()
                st.success("✅ Medicament supprimé")

        except Exception as e:
            st.error(f"❌ Erreur : {e}")
        finally:
            conn.close()
