#Clase martes 18 de junio

## NUMEROS ENTEROS = INT O LONG
##LONG se reperesenta con L al final 74874832974893L


## Numero FLOAT = NUMEROS CON DECILAMES
## EJ: 0.32
# -33.895

## COMPLEX extension de numeros reales
# 33.8j

## OPERADORES ARITMETICOS
# SUMA +
# RESTA -
# MULTIPLICACION *
# POTENCIA **
# DIVISION (cociente) /
# DIVISION (parte entera) //
# PROMEDIO %

# PROCEDENCIA DE LOS OPERADORES:
#1- TERMINOS ENTRE PARENTESIS
#2- POTENCIACION Y RAICES
#3- MULTIPLICACION Y DIVISION
#4- SUMA Y RESTA

print(15+8)

print(30.5-5)

print(80*2)



#__________________________STRING = STR (CADENA DE TEXTO)________________________

#COMILLAS DOBLES""
#COMILLAS SIMPLES '' (RECOMENDADO)

'Valentina'
#datos o caracteres que se representa

print("hola mundo")
print("un string \t con tabulacion")
print("otro  string pero con \n salto de linea")
#que es el print : imprimir, mostar algo en pantalla

#_____________________________VARIABLES_________________-
#las variables en python son como etiquetas que nospermiten hacer referencia a los datos.
#por cada dato que aparece en  un programa, python va a crear un objeto que lo contiene
#cada objeto va a tener:
#1- UN IDENTIFICADOR UNICO (id)
#2- UN TIPO DE DATO (entero, decimal, string,etc)
#3- UN VALOR (el propio dato dentro del objeto)
# LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS.

#DEFINIR UNA VARIABLE a=2 o dni=45555555
a = 2
dni = 455555555
mi_variable = 1966
print(mi_variable)

########### EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O POR UN GUION BAJO ( _ ) snake_case
## LOS NOMBRES EN LAS VARIABLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO
#PYTHON RECONOCE MAYUSCULAS Y MINUSCULAS

mi_fecha_de_nacimiento = "2004"
print(mi_fecha_de_nacimiento)

#METODO DE SALIDA = PRINT()
#METODO DE ENTRADA = INPUT()



# LA FUNCION INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADA EN UN SPRING (una cadena). AUNQUE LE ESTEMOS ESCRIBIENDO UN NUMERO


a = 20
b = 30

resultado = a+b
print(resultado)

c = 100
d = 200

print(c+d)


#LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR DE STR (STRING)
e = 30
""" f = input("cual es tu edad") """ #se comenta con alt+shift+a Esto es un ejemplo de unn dato de entrada que lo toma con cadena de texto
f= int(input("cual es tu edad"))  #CONVERSION DE TIPO: de esta forma logramos que python convierta el STR de enttrada en un NUMERO


print(e-f)

cadena_de_texto = "python"
anio_del_curso = "2024"
print(cadena_de_texto)
print(cadena_de_texto + anio_del_curso)

#A LAS SUMAS DE LOS STRING LO VAMOS A LLAMAR CARACTERIZACION

print(cadena_de_texto[-1])

#los indices van adentro de los corchetes []
#LOS INDICES VIENEN: 0 (primer caracter), 1 (segundo caracter)
#LOS INDICES INVERSOS: -1 (ultimo caracter), -2 (anteultimo caracter)
# 0 1 2 3 4 5 6 indices
# -6 -5 -4 -3 -2 -1 indice inverso
print (cadena_de_texto[-2])
