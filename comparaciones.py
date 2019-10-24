from ao import ao
from Movie import Movie
from listaPelis import listaPelis

import random

lp=listaPelis()
lp.lectura()
a=ao(lp)


b=[3500,7000,10500,14000,17500]
"""
for r in range(1):
    print ('Bubble Sort:')
    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        a=ao(s)
        s=a.bubbleSort()
        print(b[z],a.getCont())

    print ('\n\n\n')

    print('Selection Sort:')
    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        a = ao(s)
        s = a.selectionSort()
        print(b[z],a.getCont())


    print('\n\n\n')
    print('Insertion Sort:')

    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        a = ao(s)
        s = a.insertionSort()
        print(b[z],a.getCont())
"""
for i in range(1):
    print('\n\n\n')
    print('Quick Sort:')

    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        a = ao(s)
        s = a.quickSort()
        print(a.getCont())

"""
for i in range(1):
    print('\n\n\n')
    print('MergeSort:')

    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        s.reverse()
        a = ao(s)
        a.mergeSort(s)
        print(a.getCont())

"""
