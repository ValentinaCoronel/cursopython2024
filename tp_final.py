"""  ##Ejercicio 1: Números y Cadenas de Caracteres
#Escribe un programa que pida al usuario dos números enteros y realice lo siguiente:
#Muestra la suma de los dos números.
#Muestra el producto de los dos números.
#Muestra la concatenación de los dos números (como texto

#PEDIR EDAD 

edad_juan = 9
edad_sara = 8

suma = [9+8]

producto = [9*8]

texto= str(9)+str(8)

print(suma)
print(producto)
print(input(texto)) 

##Pide al usuario una cadena de texto. Luego muestra:
#La cadena en mayúsculas.
#La longitud de la cadena.
#La cadena invertida.
#La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario).

nombre = "mi nombre es juan"
print(nombre)
print(nombre.upper())
print(len(nombre))
print(nombre[::-1])
print(nombre.count("n"))

#Escribe un programa que convierta un número decimal a binario y viceversa.

numero_ = 28
binario = ""

while numero_ > 0:
    if numero_ %2 == 0:
        binario = "0" + binario
    else:
        binario = "1" + binario
        
    numero_ = numero_ // 2

print(binario)

decimal= 0

pos= len(binario)

for i in reversed(binario):
    if i == "1":
        decimal = decimal + pow(2, (len(binario) - pos))
    pos = pos - 1
    
print(decimal)



#Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero.

una_cadena = "me gusta la cerveza"
un_entero = 3
print(una_cadena*un_entero) """



#Ejercicio 2: Listas y Tuplas
#Crea una lista con los nombres de tres frutas. Luego:
#Añade dos frutas más a la lista.
#Ordena la lista alfabéticamente.
#Muestra la lista completa.
#Elimina una fruta de la lista y muestra el resultado.

verduras = ["banana", "manzana", "kiwi"]
verduras.append("naranja")
verduras.append("frutilla")
print(verduras)
verduras.sort()
print(verduras)
verduras.pop()
print(verduras)

#Crea una tupla con los nombres de dos ciudades. Luego:
#Muestra el primer y último elemento de la tupla.
#Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante.

ciudades= ("Moron", "Rafael Castillo")
print(f"La primer ciudad es: {ciudades[0]} y la última es: {ciudades[-1]}")

ciudades_lista = list(ciudades)
ciudades_lista.append("Castelar")
print(ciudades_lista)

#Crea una lista de números enteros y muestra:
#El número mayor de la lista.
#El número menor de la lista.
#El promedio de los números en la lista.

enteros = [31, 18, 16, 22, 27]
print(max(enteros))
print(min(enteros))
print(sum(enteros)/len(enteros))

#Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas.
mascotas= ["thor", "artemisa", "catalina", "indio"]
mascotas_mayusculas = [mascota.upper() for mascota in mascotas]
print(mascotas_mayusculas)


#Ejercicio 3: Controladores de Flujo
#Escribe un programa que pida un número al usuario. Muestra si el número es par o impar.
nacimiento= 2004
if nacimiento % 2 == 0:
  print(f"el numero {nacimiento} es par")
else :
  print(f"el numero{nacimiento} es impar")
  

#Crea un programa que simule un menú simple con las siguientes opciones:
#Saludar
#Despedirse
#Salir
#Dependiendo de la opción elegida, muestra un mensaje correspondiente. Si se elige 3, el programa debe terminar.

""" while True:
    print("1. Saludar\n2. Despedirse\n3. Salir")
    opcion = input("Elegir una opcion: ")
    if opcion == "1":
        print("Saludar")
    elif opcion == "2":
        print("Despedirse")
    elif opcion == "3":
        print("Salir")
        break
    else:
        print("Opción no válida, intenta de nuevo.") """



#Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero.
cumpleanios = 29
if cumpleanios > 0:
    print("el numero es positivo")
elif cumpleanios < 0:
    print("el numero es negativo")
else :
    print("el numero es 0")
    

#Escribe un programa que muestre los números del 1 al 10 utilizando un bucle for.

texto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in texto:
    print(numero) 



#Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle while
suma = 0
contador = 1
while contador <= 100:
    suma += contador
    contador += 1
print(suma)


#Ejercicio 4: Conjuntos y Diccionarios
#Crea dos conjuntos con algunos números. Luego:
#Muestra la unión de los dos conjuntos.
#Muestra la diferencia entre los dos conjuntos.
#Muestra los elementos comunes en ambos conjuntos.

conjunto_1 = {67 , 66 , 4 , 1 , 99}
conjunto_2 = {67, 3, 34}

conjunto_1.update(conjunto_2)
print(conjunto_1)

print(conjunto_1.difference(conjunto_2))
print(conjunto_1.intersection(conjunto_2))

#Crea un diccionario con tres nombres como claves y edades como valores. Luego:
#Muestra la edad del primer nombre en el diccionario.
#Añade un nuevo nombre y edad al diccionario.
#Elimina un nombre del diccionario y muestra el resultado.
#Muestra todas las claves y todos los valores del diccionario.

diccionario = { "Ezequiel" : "19", "Nery" : "79", "Lidia" : "83"}
print(diccionario["Ezequiel"])

diccionario["Monica"] = 57
print(diccionario)

diccionario.pop("Ezequiel")

print(diccionario)

#Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores. Luego:
#Muestra el precio de un producto específico.
#Incrementa el precio de todos los productos en un 10%.
#Muestra el diccionario actualizado.

productos = {"leche" : 100, "yerba" : 300, "azucar" : 50, "sal" : 20, "aceite" : 500}
print(productos["aceite"]) 

productos_actualizados = {producto: precio * 1.10 for producto, precio in productos.items()}

print("Lista de precios actualizada con aumento de 10%:")
for producto, precio in productos_actualizados.items():
    print(f"{producto}: {precio:.2f}")


#Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Muestra:
#La intersección de los dos conjuntos.
#La diferencia simétrica entre los dos conjuntos.

numeritos = {1, 2, 3, 4, 5}
numerotes = {4, 5, 6, 7, 8}
print(numeritos.intersection(numerotes))
print(numeritos.difference(numerotes))
print(numerotes.difference(numeritos))

#Ejercicio 5: Funciones
#Define una función saludar(nombre) que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre.
#Define una función suma(a, b) que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.
#Define una función es_mayor_de_edad(edad) que reciba una edad y retorne True si la edad es mayor o igual a 18 y False en caso contrario. Prueba la función con diferentes edades.


def saludar (Ezequiel):
    print("Hola Ezequiel como estas")
    return saludar
print("Hola Valentina como estas")

def suma(a, b):
    return a + b

# Probar la función suma con dos números diferentes
resultado_suma = suma(5, 7)
print(f"La suma de 5 y 7 es: {resultado_suma}")

# Definir una función es_mayor_de_edad que reciba una edad y retorne True o False
def es_mayor_de_edad(edad):
    return edad >= 18

# Probar la función es_mayor_de_edad con diferentes edades
edad1 = 20
edad2 = 16

print(f"¿La persona con {edad1} años es mayor de edad? {es_mayor_de_edad(edad1)}")
print(f"¿La persona con {edad2} años es mayor de edad? {es_mayor_de_edad(edad2)}")
