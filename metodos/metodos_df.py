from unidecode import unidecode
import streamlit as st

def validar_mesa(mesa):
    try:
        int(mesa)
        return True
    except ValueError:
        return False
    
def validar_nombre(nombre):
    return isinstance(nombre, str)

def validar_cantidad(cantidad):
    return isinstance(cantidad, int)

def validar_telefono(telefono):
    return isinstance(telefono, str)

def procesa_lista(df):
    """
    Procesa el dataframe creado a partir del CSV.

    Argumentos:
    df: pandas dataframe creado a partir del archivo csv

    Retorna:
    df: pandas dataframe ya limpio
    """
    mesa_valida = df['Mesa'].apply(validar_mesa)
    nombre_valido = df['Nombre'].apply(validar_nombre)
    cantidad_valida = df['Cantidad'].apply(validar_cantidad)
    telefono_valido = df['Telefono'].apply(validar_telefono)

    df['Nombre'] = df['Nombre'].str.lower()
    df['Nombre'] = df['Nombre'].apply(unidecode)

    return df

def busqueda_lista(lista, opcion, buscar):
    """
    Hace busquedas en el dataframe lista para encontrar la mesa asignada y la cantidad de persoans admitidas.

    Argumentos:
    lista: pandas dataframe creado a partir del archivo csv
    opcion: opcion de busqueda por defecto el telefono pero pudiera ser por nombre

    Retorna:
    .
    """
    if opcion == 'Telefono':
        opcion = 1
        fila = lista[lista['Telefono'] == buscar]
        st.write(fila)
    if opcion == 'Nombre':
        opcion = 2
        fila = lista[lista['Nombre'].str.contains(buscar, case=False)]
        st.write(fila)

    if not fila.empty:
        # Si se encontró, obtener la mesa y la cantidad
        mesa = fila['Mesa'].iloc[0]
        cantidad = fila['Cantidad'].iloc[0]
        comentarios = fila['Comentarios'].iloc[0]
        nombre = fila['Nombre'].iloc[0]
        nombre = nombre.title()
        return nombre, mesa, cantidad, comentarios
    else:
        st.error(f"No se encontraron registros para el cliente {buscar}.")
