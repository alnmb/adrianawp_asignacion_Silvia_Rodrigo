import streamlit as st

st.set_page_config(
    page_title="Asignacion de mesas - Home",
)
# logo de adriana
st.image("img/LOGO AMEP MORADO.png")
st.header("Asignacion de mesas - Boda Silvia & Rodrigo")
st.subheader("Fecha: Sabado 18 de Mayo 2024")

if __name__ == '__main__':
    st.page_link("pages/busqueda.py", label="Busqueda", icon="🔍")
