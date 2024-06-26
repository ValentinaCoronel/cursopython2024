""" #Longitud de String
# Funcion LEN sirve para contabilizar los caracteres de un string

esto_es_un_string = "hola soy un string"

print(len(esto_es_un_string))

string1= "    "
print(len(string1))


#Funncion para rebanar un string
#Funcion SLICING [inicio:fin:paso]
#sirve para tomar una parte de lo que hay en un string 
#Inicio va a ser el indice del primer caracter de la cadena ue queremos rebanar o seleccionar
#Fin va a ser el indice del ultimo caracter no incluido de la cadena q queremos rebanar
#Paso nos indica cada cuantos caracteres vamos a seleccionar entre las posiciones de inicio y fin

saludo = "hola, como estas"
print(len(saludo))
saludo[0:3:1]
print(saludo[0:3:1])
print(saludo[0:17:2])


palabra = "Pithon"
print(palabra)

print(palabra[1])
#los string no se puede sustituir los caracteres de manera individual, pero si reasignarlo  de la sig manera
palabra = palabra[0:1] +"y"+ palabra[2:]
print(palabra)


### LISTA Y TUPLAS

mi_lista = [-11,20,3,41]
print(mi_lista)

otra_lista = ["hola","Como","Estas","?"]

variable_1 = "Una variable"

listita = [1,-10,13.5,"Un string", "Otro string", variable_1]
print(listita)

print(listita[0])
print(listita[-1])

print(listita[-2:])


listita + [otra_lista, "ALGO RANDOM"]
print(listita + [otra_lista, "ALGO RANDOM"])

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,16])

numeros = [0,2,4,5,10,15,20]
numeros[3] = 8
print(numeros)


letras = ["a","b","c","d","e","f"]
letras[:3] = ["A","B","C"]
print(letras)

letras = ["a","b","c","d","e","f"]
letras[:3] = []
print(letras)

equipos = ["Moron","River","Boca","Independiente"]
print(equipos)
equipos =[]
print(equipos) """

#FUNCION APPEND
#permite agregar un nuevo item pero al final de la lista- Se escribe mi_lista.append(item_a_agregar) (se puede hacer op o simples num)

numeros =[1,2,3,4,5,6]
numeros.append(7*2)
print(numeros)

#Tambien podemos utilizar la funcion LEN acá
print(len(numeros))


#FUNCION POP
#es todo lo contrario a Append, porque va a eliminar el ultimo item de una lista. Se escribe: pop.()
equipos = ["Moron","River","Boca","Independiente"]
equipos.pop()
print(equipos)
##########Si ingreso dentro del parentesis una posicion segun indice, POP eliminara el indice correspondiente
equipos = [1,2,3,4,5]
equipos.pop(2)
print(equipos)



#FUNCION COUNT
#La funcion count cuenta el numero de veces que nuestro item se repite dentro de una lista. Se escribe: la_lista_a_contar.count(el_item_que_queremos_que_se_cuente)
#en este caso el item 20 se repite tres veces
numeros_varios = [1,2,3,4,5,9,12,55,20,20,20,3,5,29]
print(numeros_varios.count(20))


#FUNCION INDEX
#busca  el item y nos devuelve en que indice esta. Se escribe: la_lista.index(lo_que_queremos_buscar)
numeros_varios = [1,2,3,5,9,12,55,20,20,20,3,5,59]
print(numeros_varios.index(59))



#___________________TUPLAS
#son parecidas a las listas, con la diferencia que son inmutables. Son heterogeneas, no tienen restricciones en cuanto a items
#se declran con parentesis- mi_tuplaa(1,2,3,4)

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

tupla = (1,)

print(tupla) 
 
otra_tupla = (1,5,-10,"Cadena","Otra cadena/string",mi_tupla)
print(otra_tupla)

print(otra_tupla[0])

print(otra_tupla[2:])

#podemos aplicar las funciones de la siguiente manera
print(len(otra_tupla))

print(otra_tupla.index(5))

print(otra_tupla.count(1))
