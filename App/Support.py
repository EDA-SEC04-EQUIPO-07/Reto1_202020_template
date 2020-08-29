#imports

import config as cf
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

#sorted implementado

def sort(lst, criteria, opcion): 
    if criteria.lower() in 'vote_average':
        if opcion == '1':
            mergesort(lst, lessfunction='lessfunctionAvrg')
        elif opcion == '2':
            mergesort(lst, lessfunction='greaterfunctionAvrg')
    elif criteria.lower() in 'vote_count':
        if opcion == '1':
            mergesort(lst, lessfunction='lessfunctionCount')
        elif opcion == '2':
            mergesort(lst, lessfunction='greaterfunctionCount')

#sorted

def lessfunctionCount(element1, element2):
    element1=element1['vote_count']
    element2=element2['vote_count']
    if element1 == element2:
        return 0
    elif element1 < element2:
        return 1
    else: 
        return -1

def greaterfunctionCount(element1, element2):
    element1=element1['vote_count']
    element2=element2['vote_count']
    if element1 == element2:
        return 0
    elif element1 > element2:
        return 1
    else: 
        return -1

def lessfunctionAvrg(element1, element2):
    element1=element1['vote_average']
    element2=element2['vote_average']
    if element1 < element2:
        return 1
    elif element1 == element2:
        return 0
    else: 
        return -1

def greaterfunctionAvrg(element1, element2):
    element1=element1['vote_average']
    element2=element2['vote_average']
    if element1 > element2:
        return 1
    elif element1 == element2:
        return 0
    else: 
        return -1
    
#Funciones de apoyo

def findmoviesDirector(director_name, lst):
    """
    retorna:
        -lista de peliculas del director pasado por parametro.
    """
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie= it.next(iterator)
        if director_name.lower() in movie['director_name'].lower():
            info_movies.append(movie)
    return info_movies

def findmoviesActor(actor_name, lst):
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        if actor_name.lower() in movie['actor1_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor2_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor3_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor4_name'].lower():
            info_movies.append(movie)
        elif actor_name.lower() in movie['actor5_name'].lower():
            info_movies.append(movie)
    return info_movies
    
def findmoviesGenre(genre, lst):
    """
    Retorna:
        -lista de peliculas que tienen en su genero 
    """
    info_movies=[]
    iterator=it.newIterator(lst)
    while it.hasNext(iterator):
        movie=it.next(iterator)
        if genre.lower() in movie['genres'].lower():
            info_movies.append(movie)
    return info_movies

def findmovieId(Id, lst):
    """
    Retorna:
        -El diccionario de la pelicula que tiene ese ID.
    """
    iterator=it.newIterator(lst)
    found=False
    dic=None
    while it.hasNext(iterator) and not found:
        movie=it.next(iterator)
        if movie['id'] == Id:
            found=True
            dic=movie
    if found == True:
        return movie
    else:
        return ('No movie match with ID')

                 
#sorting

def mergesort(lst, lessfunction):
    size = lt.size(lst)
    if size > 1:
        mid = (size// 2 )
        #se divide la lista original, en dos partes, izquierda y derecha, desde el punto mid.
        leftlist = lt.subList (lst, 1, mid)
        rightlist = lt.subList (lst, mid+1, size - mid )

        #se hace el llamado recursivo con la lista izquierda y derecha
        mergesort (leftlist, lessfunction)
        mergesort (rightlist, lessfunction)

        #i recorre la lista izquierda, j la derecha y k la lista original
        i=j=k=1
        
        leftelements = lt.size (leftlist)
        rightelements = lt.size (rightlist)
   
        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist,i)
            elemj = lt.getElement(rightlist,j)
            #compara y ordena los elementos
            if lessfunction (elemj, elemi):   # caso estricto elemj < elemi
                lt.changeInfo(lst, k, elemj)
                j += 1
            else:                                              # caso elemi <= elemj
                lt.changeInfo (lst, k, elemi)
                i += 1
            k += 1
            
        #Agrega los elementos que no se comprararon y estan ordenados
        while i <= leftelements:
            lt.changeInfo(lst, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lst, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
