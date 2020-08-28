#imports

from DataStructures import listiterator as it
from DataStructures import liststructure as lt

#sorted
def cmpfuction(element1, element2, opcion):
    if opcion == '1':
        lessfunction(element1, element2)
        
    elif opcion == '2':
        greaterfunction(element1, element2)



def lessfunction(element1, element2, criteria):
    if element1 == element2:
        return 0
    elif element1 < element2:
        return 1
    else: 
        return -1

def greaterfunction(element1, element2, criteria):
    if element1 == element2:
        return 0
    elif element1 > element2:
        return 1
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
            info_movies.append(movie["id"])
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
                 