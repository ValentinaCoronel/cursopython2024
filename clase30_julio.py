#            conjuntnoys / SET
conjunto = {1,2,3,4,5}
otro_conjunto = {"hola", "como", "estas" , "?"}
conjunto_vacio = set()

#son heterogeneos
variable1 = "esto es una variables"
datos = {1,-5,123,57, "una cadena", "otro string", variable1}
print(datos)

#Puede incluir numeros, variables, strings o tuplas.
#Pero NO puede incluir objetos mutables como listas, diccionarios e incluso otros conjuntos.


lista = ((1,2,3,4,5))
print(lista)
print(set([1,1,2,2,2,3,3,4,4]))
#las listas y set sonmutables, pero  los set no se pueden manejar por ejemplo por indice

#FUNCIONES INTEGRADAS EN SET/CONJUNTOS
numeros = {1,2,3,4,}
numeros.add(5)
print(numeros)


#update
numeros = {1,2,3,4}
numeros.update([5,6,7,8])
print(numeros)

#len
print(len(numeros))

#discard
numeros.discard(2)
print(numeros)

#REMOVE
#REMOVE Y DISCARD funciona de igual manera, a diferencia que en discard si el elemento pasado como argumento no existe, lo ignora. En cambio en Remove nos devolvera un error.


#IN
print(3 in numeros)

#CLEAR
numeros.clear()

#POP
""" numeros1 = {1,2,3,4,5,6}
while numeros1:
    print("se esta borrando", "numeros1.pop()")
     """
#DICCIONARIO/DICT
          
colores= {"amarillo": "yellow", "azul": "blue", "rojo":"red"}

print(colores["amarillo"])
          
colores["amarillo"] = "white"
print(colores)

edades= {"Juan":26, "Esteban":35, "Maria":29}
edades["Juan"] +=5
edades["Maria"] *=2
print(edades)


#ADD
numeros3 = {"uno":1, "dos":2, "tres":3, "cuatro":4}
numeros3["cinco"]=5
print(numeros3)

#UPDATE
numeros3.update({"seis":6})
print(numeros3)

#LEN
print(len(numeros3))

#DEL
del numeros3["dos"]
print(numeros3)

#IN
"dos" in numeros3
print("dos" in numeros3)

#CLEAR
numeros3.clear()

""" #POP
print(numeros3.pop("uno")) """
 
#UPPER
cadena = "Hola chicos"
print(cadena.upper())
print("Hola como estan".upper())

#LOWER
string = "HOLA CHICOS"
print(string.lower())

#CAPITALIZE
cadena1 ="hola amigos"
print(cadena1.capitalize())

""" #TITTLE
cadena2 = "hola Mundo"
print(cadena2.tittle()) """

#COUNT
cadena3 = "hola Mundo esta cadena tiene muchas a"
print(cadena3.count("a"))

#FIND
cadena4 = "hola Mundo esta cadena tiene muchas a"
print(cadena4.find("Mun"))

#RFIND
cadena5 = "hola amigo como estas amigo"
print(cadena5.find("amigo"))
print(cadena5.rfind("amigo"))

#SPLIT
cadena6 = "hola MUNdo"
print(cadena6.split())

#JOIN
cadena7 = "hola mundo"
print("x".join(cadena7))

#strip
cadena8 = "---------hola mundo---------"
print(cadena8)
print(cadena8.strip("-"))

cadena8= "      hola mundo"
print(cadena8)
print(cadena8.strip())

#REPLACE
cadena9 ="Moron"
print(cadena9.replace("o", "0"))

#            METODOS PARA LISTAS
#CLEAR

letras = ["a", "b", "c", "d", "e", "f"]
print(letras)
letras.clear()
print(letras)

#EXTEND
numeros = [1,2,3,4,5]
numeros + [6,7,8,9]

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9]

lista1.extend(lista2)
print(lista1)

#INSERT inserta el valor que quiera luego de "," en el indice indicado antes de la ","
lista3 = [1,2,3,4,5,6]
lista3.insert(0,0)
print(lista3)

#REVERSE da vuelta la lista
lista4 = [1,2,3,4,5,6]
lista4.reverse()
print(lista4)

#SORT ordena de menor a mayor
lista5 = [5,-10,35,0,-75,150]
lista5.sort()
print(lista5)



#      CONJUNTOS
#COPY nos devuelve una copia del set x a o x b
set1 = {1,2,3,4}
set2 = set1.copy()
print(set2)

#ISDISJOINT nos indica si es distinto 
set3 = {1,2,3}
set4 = {3,4,5}
print(set1.isdisjoint(set2))

#ISSUBSET indica si esta dentro del otro set
set5= {-1,99}
set6 = {1,2,3,4,5}
print(set5.issubset(set6))

#ISSUPERSET comprueba si el set contiene todos los items del otro
set7 = {1,2,3}
set8 = {1,2}
set7.issuperset(set8)
print(set7.issuperset(set8))

#UNION une un set con otro
set9 = {1,2,3}
set10 = {3,4,5}
set11 = set9.union(set10)

#DIFFERENCE
set12 = {1,2,3}
set13 = {3,4,5}
print(set12.difference(set13))

#DIFFERENCE_UPDATE
set12 = {1,2,3}
set13 = {3,4,5}
set12.difference_update(set13)
print(set12)

#INTERSECTION
set14 = {1,2,3}
set15 = {3,4,5}
set14.intersection(set15)
print(set14.intersection(set15))

#INTERSECTION_UPDATE
set14 = {1,2,3}
set15 = {3,4,5}
set14.intersection_update(set15)
print(set14)




#DICCIONARIOS 
#GET busca un elemento a traves de su clave, si no lo encuentra nos devuelve un valor por defecto que  le indiquemos
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.get("verde", "no hay clave verde"))

#KEYS sirve para traer todas las claves de un diccionario en el caso de desconocerlas
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.keys())

#VALUES sirve para traer todos los valores del diccionario como tal
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.values())

#ITEMS crea una lista con clave y valor de los items de un diccionario
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.items())


for clave, valor in colores.items():
    print(clave,valor)
    













