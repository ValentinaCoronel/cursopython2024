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
for num in (1,2,3,4,5,6,7,8,9,10):
    print(num)
    

