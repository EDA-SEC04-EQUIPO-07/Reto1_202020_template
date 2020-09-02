"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""
#imports

import config as cf
import sys
import csv
import Support as sup

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from time import process_time 

#Funciones

def compareRecordIds(recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1


def loadCSVFile (file, lst):
    lst=lt.newList(datastructure="ARRAY_LIST")
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        with open( file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies (file, lst):
    lst = loadCSVFile(file, lst) 
    print("Datos cargados, " + str(lt.size(lst)) + " elementos cargados")
    return lst

def FindGoodMovie(lst,lst2,name_director):
    "Retorna: el numero de películas buenas de un director y su promedio de la votación."
    list_movies=[]
    info_movies= sup.findmoviesDirector(name_director, lst)
    avgsum=0
    for movie in info_movies:
        movie_data=sup.findmovieId(movie['id'], lst2)
        if movie_data["vote_average"] >= 6:
            list_movies.append(movie_data['title'])
            avgsum+=float(movie_data['vote_average'])
    size=len(list_movies)
    avg=avgsum/size
    return(size,avg)



def rankingMovies(lst, criteria, opcion):
    """
    Genera rankings de acuerdo a las condiciones puestas.

    Arg:
        lst :: list
            -La informacion de detallada de las peliculas.
        criteria :: str
            -Criterio de ordenamiento
        opcion :: int
            -Determina si se ordena de menor a mayor o de mayor a menor
            1,2 respectivamente
    
    Retorna :: list
        -TAD list con el catalogo pedido.
    """
    catalog=lt.newList(datastructure='ARRAY_LIST')
    sup.sort(lst, criteria, opcion)
    if opcion == '1':
        i=0
        while i < 5:
            movie=lt.getElement(lst, i)
            lt.addLast(catalog, movie['title'])
            i+=1
    elif opcion == '2':
        i=0
        while i < 10:
            movie=lt.getElement(lst, i)
            lt.addLast(catalog, movie['title'])
            i+=1
    return catalog



def SearchbyDirector(lst,lst2,name_director):
    """
    Busca todas las peliculas en las que un director trabajo.
    Arg:
        -lst :: list 
            La informacion en bruto de las peliculas.
        -lst2 :: list 
            La informacion especifica de las peliculas.
        -name_director :: str
            El nombre del director.
    
    Retorna :: tuple 
        -Todas las películas dirigidas, El numero de las películas 
        y El promedio de la calificación de sus películas.
    """
    avgsum= 0
    info_movies=sup.findmoviesDirector(name_director, lst)
    size=len(info_movies)
    list_movies=[]
    for movie in info_movies:
        movie_data=sup.findmovieId(movie['id'], lst2)
        list_movies.append(movie_data['title'])
        avgsum+=float(movie_data['vote_average'])
    avg=avgsum/size
    return(list_movies,size,avg)

def SearchbyActor(lst,lst2,actor_name):
    """
    Busca todas las peliculas en las que un actor participo.
    Arg:
        -lst :: list 
            -La informacion en bruto de las pelicula.
        -lst2 :: list
            -La informacion especifica de las peliculas.
        -actor_name :: str 
            -Nombre del actor buscado
    retorna :: tuple 
        -Todas las películas en las que actuo, el numero de las películas, 
        el promedio de calificacion y el director con el que mas trabajo en ese orden.
    """
    avgsum= 0
    info_movies=sup.findmoviesActor(actor_name, lst)
    size=len(info_movies)
    list_movies=[]
    dict_directors={}
    for movie in info_movies:
        print(movie)
        print(size)
        name_director=movie['director_name']
        movie_data=sup.findmovieId(movie['id'], lst2)
        list_movies.append(movie_data['title'])
        avgsum+=float(movie_data['vote_average'])
        if name_director in dict_directors.keys():
            dict_directors[name_director]+=1
        else:
            dict_directors[name_director]=1
    director= max(dict_directors)
    avg=round(avgsum/size,2) 
    return(list_movies,size,avg,director)

def meetGenre(lst, lst2, genre):
    """
    Busca todas las peliculas que corresponden al genero dado por parametro.
    Arg:
        lst :: list
            -La informacion en bruto de las peliculas.
        lst2 :: list
            -La informacion especifica de las peliculas.
        genre :: str
            -El genero que se desea buscar.
    Retorna :: tuple
        -El titulo de las peliculas, el numero de peliculas y la votacion promedio en ese orden.
    """
    avgsum=0
    info_movies=sup.findmoviesGenre(genre, lst2)
    list_movies=[]
    size=len(info_movies)
    i=0
    while i < size:
        list_movies.append(info_movies[i]['title'])
        avgsum+=float(info_movies[i]['vote_count'])
        i+=1
    avgsum=round(avgsum/size,2)
    return(list_movies, size, avgsum)

def moviesbygenre(lst2,genre,opcion,criteria):
    """
    Genera rankings de acuerdo a las condiciones puestas.

    Arg:
        lst2 :: list
            -La informacion de detallada de las peliculas.
        genre: str
            - Genero de la pelícla
        criteria :: str
            -Criterio de ordenamiento(vote_count o vote_avarage)
        opcion :: int
            -Determina si se ordena de menor a mayor o de mayor a menor
            1,2 respectivamente
    
    Retorna :: list
        -TAD list con el catalogo pedido.
        -float: promedio de votos
    """
    
    catalog=lt.newList(datastructure='ARRAY_LIST')
    listbygenre=sup.findmoviesGenre(genre,lst2)
    sup.sort(listbygenre, criteria, opcion)
    avgsum=0
    if opcion == '1':
        i=0
        while i < 5:
            movie=lt.getElement(listbygenere, i)
            lt.addLast(catalog, movie['title'])
            avgsum+=float(info_movies[i][criteria])
            i+=1
    elif opcion == '2':
        i=0
        while i < 10:
            movie=lt.getElement(listbygenre, i)
            lt.addLast(listbygenre, movie['title'])
            avgsum+=float(info_movies[i][criteria])
            i+=1
    avgprom= avgsum/i
    return (catalog,avgprom)


#menus

def submenu2():
    """
    Imprime el menu de la segunda opcion
    """
    print('Criterios de ordenamiento:\n')
    print('\t-1) \"vote_average\" : ordenar por la votacion promedio.')
    print('\t-2) \"vote_count\" : ordenar por cantidad de votos.')
    print('Elija un orden de ordenamiento:\n')
    print('\t-1) Top 5 peores en el criterio seleccionado.')
    print('\t-2) Top 10 mejores en el criterio seleccionado.')

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Ranking de peliculas")
    print("3- Conocer un director")
    print("4- Conocer un actor")
    print("5- Entender un genero")
    print("6- Crear ranking")
    print("0- Salir")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista_1=[]
    lista_2=[]
    best_10=[]
    worst_5=[]
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                print('1- Carga la informacion del casting de las peliculas\n')
                print('2- Carga la informacion detallada de las peliculas\n')
                opcion=input('Selecione la lista de datos que desea cargar\n')
                if opcion == '1':
                    lista_1=loadMovies('Data\moviesdb\MoviesCastingRaw-small.csv', lista_1)
                elif opcion == '2':
                    lista_2=loadMovies('Data\moviesdb\SmallMoviesDetailsCleaned.csv', lista_2)
                else:
                    print('Esa opcion no es valida')
            elif int(inputs[0])==2: #opcion 2
                submenu2()
                criteria=input('Escoja un criterio de ordenamiento:\n')
                opcion=input('Escoja un orden:\n')
                if criteria == '1':
                    if opcion == '1':
                        worst_5=rankingMovies(lista_2, criteria, opcion)
                        cadena=','.join(worst_5)
                        print('Las peores 5 peliculas segun su votacion promedio son: ', cadena)
                        i=0
                        while i < lt.size(worst_5):
                            print(lt.getElement(worst_5,i))
                            i+=1       
                    elif opcion == '2':
                        best_10=rankingMovies(lista_2, criteria, opcion)
                        cadena=','.join(best_10)
                        print('Las mejores 10 peliculas segun su votacion promedio son: ', cadena)
                        i=0
                        while i < lt.size(best_10):
                            print(lt.getElement(best_10,i))
                            i+=1
                    else:
                        print('La opcion: \"', opcion,'\" no es una opcion valida')
                elif criteria == '2':
                    if opcion == '1':
                        worst_5=rankingMovies(lista_2, criteria, opcion)
                        cadena=','.join(worst_5)
                        print('Las peores 5 peliculas segun su cantidad de votos son: ')
                        i=0
                        while i < lt.size(worst_5):
                            print(lt.getElement(worst_5,i))
                            i+=1       
                    elif opcion == '2':
                        best_10=rankingMovies(lista_2, criteria, opcion)
                        print('Las mejores 10 peliculas segun su cantidad de votos }son: ')
                        i=0
                        while i < lt.size(best_10):
                            print(lt.getElement(best_10,i))
                            i+=1
                    else:
                        print('La opcion: \"', opcion,'\" no es una opcion valida')
                else:
                    print(criteria, 'No es una opcion valida.')
            elif int(inputs[0])==3: #opcion 3
                director_name=input('Digite el nombre del director:\n')
                (movies_director, size, avg)=SearchbyDirector(lista_1, lista_2, director_name)
                print('La cantidad de peliculas del director son: ', str(size), 'y tiene una votacion promedio de: ', str(avg),'.')
                print('Las peliculas en las que participo fueron:\n')
                cadena=','.join(movies_director)
                print(cadena)
            elif int(inputs[0])==4: #opcion 4
                actor_name=input('Digite el nombre del actor:\n')
                (movies_actor, size, avg, director)=SearchbyActor(lista_1, lista_2, actor_name)         
                print('La cantidad de peliculas en las que participo el actor son: ', str(size), 'y tiene una votacion promedio de: ', str(avg),'.')
                print('El director con el que más trabajo fue: ', director)
                print('Las peliculas en la que participo fueron:\n')
                cadena=','.join(movies_actor)
                print(cadena)
            elif int(inputs[0])==5: #opcion 5
                genre=input('Digite un genero para buscar:\n')
                (movies_genre, size, avg)=meetGenre(lista_1, lista_2, genre)
                print('La cantidad de peliculas encontradad para el genero: \"', genre,'\" son: ', str(size), 'y tiene una votacion promedio de: ', str(avg),'.')
                print('Los titulos son:\n')
                cadena=','.join(movies_genre)
                print(cadena)

            elif int(inputs[0])==6: #opcion 6
                genre= input("Escoja un género:\n")
                criteria=input('Escoja un criterio de ordenamiento:\n')
                opcion=input('Escoja un orden:\n')
                if criteria == '1':
                    if opcion == '1':
                        worst_5_va=moviesbygenre(lst2, genre, opcion, criteria)
                        print('Las peores 5 peliculas segun su votacion promedio son: ')
                        print("el promedio de votación es: "+ str(worst_5_va[1]))
                        i=0
                        while i < lt.size(worst_5_va[0]):
                            print(lt.getElement(worst_5_va[0],i))
                            i+=1       
                    elif opcion == '2':
                        best_10_va=moviesbygenre(lst2, genre, opcion, criteria)
                        print('Las mejores 10 peliculas segun su votacion promedio son: ')
                        print("el promedio de votación es: "+ str(best_10_va[1]))
                        i=0
                        while i < lt.size(best_10_va[1]):
                            print(lt.getElement(best_10_va[1],i))
                            i+=1
                    else:
                        print('La opcion: \"', opcion,'\" no es una opcion valida')
                elif criteria == '2':
                    if opcion == '1':
                        worst_5_vc=moviesbygenre(lst2, genre, opcion, criteria)
                        print('Las peores 5 peliculas segun su cantidad de votos son: ')
                        print("el promedio de votación es: "+ str(worst_5_vc[1]))
                        i=0
                        while i < lt.size(worst_5_vc[0]):
                            print(lt.getElement(worst_5_vc[0],i))
                            i+=1       
                    elif opcion == '2':
                        best_10_vc=moviesbygenre(lst2, genre, opcion, criteria)
                        print('Las mejores 10 peliculas segun su cantidad de votos son: ')
                        print("el promedio de votación es: "+ str(best_10_vc[1]))
                        i=0
                        while i < lt.size(best_10_vc[0]):
                            print(lt.getElement(best_10_vc[0],i))
                            i+=1
                    else:
                        print('La opcion: \"', opcion,'\" no es una opcion valida')


            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                

if __name__ == "__main__":
    main()