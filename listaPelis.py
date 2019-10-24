__author__ = 'mperezcs'
from Movie import Movie
from ao import ao
from ao import ao
import random

class listaPelis:

    __lista = []


    def __init__(self):
        self.__lista = []

    def getLista(self):
        return self.__lista

    def lectura(self):
        a=ao(self.__lista)
        pelis = open('movie_titles', 'r')
        while True:
            linea = pelis.readline()
            if not linea:
                break
            arre = linea.split(",", 2)
            m = Movie(int(arre[0]), arre[1], arre[2])
            self.__lista.append(m)
            #random.shuffle(self.__lista)
            self.__lista.sort()#para la primera prueba
            self.__lista.reverse() #para la segunda prueba: inversamente ordenado
        return self.__lista



    def listaPelisNele(self, n):
        s=[]
        i=0
        for i in range(n):
            s.append(self.__lista[i])

        return s
