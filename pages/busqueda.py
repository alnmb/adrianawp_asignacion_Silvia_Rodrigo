import streamlit as st
from metodos.metodos_xlsx import read_xlsx, update_lista
from metodos.metodos_df import procesa_lista, busqueda_lista
import os

def print_resultado(resultado: tuple):
    if len(resultado) != 0:
        st.subheader(f"Invitado: {resultado[0]}")
        st.subheader(f"Mesa: {resultado[1]}")
        st.subheader(f"#de Invitados {resultado[2]}")
        st.subheader(f"Comentarios:  {resultado[3]}")

def validate_fuente_folder():
    folder_path = "fuente"
    xlsx_files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]
    if len(xlsx_files) == 0:
        return False
    else:
        return True

def main():
    telefono = ""
    nombre = ""
    validar = validate_fuente_folder()
    if validar == True:
        lista = read_xlsx()
        lista_procesada = procesa_lista(lista)
        
        tipo_busqueda = st.selectbox("Seleccione la opcion a buscar", ("Telefono", "Nombre"), index=None, placeholder="Elija una opcion")
        
        if tipo_busqueda == "Telefono":
            telefono = st.text_input("Ingrese numero de telefono")
        if tipo_busqueda == "Nombre":
            nombre = st.text_input("Ingrese el nombre a buscar")

        if telefono != "":
            telefono = int(telefono)
            resultado = busqueda_lista(lista_procesada, tipo_busqueda, telefono)
            print_resultado(resultado)

            invitados_recibidos = st.text_input("Ingrese el numero de invitados que llegaron: ")
            if invitados_recibidos:
                invitados_recibidos = int(invitados_recibidos)
                update_lista(lista_procesada, telefono, invitados_recibidos, tipo_busqueda)
        if nombre != "":
                nombre = nombre.lower()
                resultado = busqueda_lista(lista_procesada, tipo_busqueda, nombre)
                print_resultado(resultado)
                invitados_recibidos = st.text_input("Ingrese el numero de invitados que llegaron: ")
                if invitados_recibidos:
                    invitados_recibidos = int(invitados_recibidos)
                    update_lista(lista_procesada, nombre, invitados_recibidos, tipo_busqueda)
    if validar == False:
        st.error("No hay archivo csv en el folder csv")

if __name__ == '__main__':
    main()
