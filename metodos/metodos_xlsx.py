import pandas as pd
import streamlit as st

def read_xlsx():
    folder_path = "fuente/lista.xlsx"
    df = pd.read_excel(folder_path)
    return df

def update_lista(lista_procesada, buscar, invitados_recibidos, tipo_busqueda):
    if tipo_busqueda == "Telefono":
        fila = lista_procesada[lista_procesada[tipo_busqueda] == buscar]
    elif tipo_busqueda == "Nombre":
        fila = lista_procesada[
            lista_procesada[tipo_busqueda].str.contains(buscar, case=False)
        ]
    st.write("Antes:")
    st.write(fila)
    if not fila.empty:
        lista_procesada.at[fila.index[0], "Conteo"] = invitados_recibidos
        if tipo_busqueda == "Telefono":
            fila = lista_procesada[lista_procesada[tipo_busqueda] == buscar]
        elif tipo_busqueda == "Nombre":
            fila = lista_procesada[
                lista_procesada[tipo_busqueda].str.contains(buscar, case=False)
            ]

        st.write("Despues")
        st.write(fila)

        lista_procesada.to_excel("fuente/lista.xlsx", index=False)
        st.page_link("home.py", label="Home", icon="🏠")