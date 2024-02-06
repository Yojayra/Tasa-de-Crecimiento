# Variable de texto
mi_variable ="Hola, soy Yojayra y estoy muy feliz de aprender python"
print(mi_variable)

#Lista de números
mi_lista= [1, 2, 3, 4, 5]
print(mi_lista)

#Diccionarios tipo de objeto que da una etiqueta a un valor
diccionario={"clave_1":"valor1", "clave_2": "valor2", "clave_3": "valor3"}
print(diccionario)

###############
# Replica el número 20 veces y lo presenta en un vector
vector_enteros = [10]*20 
print(vector_enteros)

vector_flotantes = [3.14]*5
print(vector_flotantes)

diccionario_2 = {"entero": vector_enteros, "flotantes": vector_flotantes, "complejos": vector_flotantes}
print(diccionario_2)

#Cadenas
cadena_simple = "Hola mundo" #Una sola variable
cadena_doble = {"PYTHON ES PODEROSOS", "ME GUSTA"} # tiene dos variables
print(cadena_doble)

##################################
#data Frame
import pandas as pd
# Muestra una base de datos por columnas
datos = {
    'Nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'Juego 1 (puntos)': [150, 180, 130, 200],
    'Juego 2 (puntos)': [120, 90, 110, 150],
    'Juego 3 (puntos)': [200, 160, 180, 190]
}

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print(df)

#####################################
# Práctica 1
#Librerías
import pandas as pd
import xlrd as x

base_sri = pd.read_excel("Datos/IMP_SRI.xlsx")
print(base_sri)
