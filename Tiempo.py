from ao import ao
from Movie import Movie
from listaPelis import listaPelis
import time
import random
lp=listaPelis()
lp.lectura()
tiempo=0
comp=0
b=[3500,7000,10500,14000,17500]


for i in range(30):
    for z in range(len(b)):
        s=lp.listaPelisNele(b[z])
        a=ao(s)
        t0=time.time()
        s=a.bubbleSort()
        tiempo=tiempo+(time.time()-t0)
        comp=comp+a.getCont()
print("Bubble Sort: ", tiempo/30, comp/30)

tiempo=0
comp=0
print('\n\n\n')
#selection
for i in range(30):
    for z in range(len(b)):
        s = lp.listaPelisNele(b[z])
        a = ao(s)
        t0=time.time()
        s = a.selectionSort()
        tiempo=tiempo+(time.time()-t0)
        comp=comp+a.getCont()
print('Selection Sort: ', tiempo/30, comp/30)
"""
tiempo=0
comp=0
print('Insertion Sort')
#insertion sort

for z in range(len(b)):
    for i in range(30):
        s = lp.listaPelisNele(b[z])
        random.shuffle(s)
        a = ao(s)
        t0=time.time()
        s = a.insertionSort()
        tiempo=tiempo+(time.time()-t0)
        comp=comp+a.getCont()
        print(b[z],i)
    print('Insertion Sort',b[z],tiempo/30, comp/30)
"""
tiempo=0
com=0
print('\n\n\n')
print('Quick Sort:')

for z in range(len(b)):
    #for i in range(30):
    s = lp.listaPelisNele(b[z])
    #s.reverse
    #random.shuffle(s)
    #s.reverse()
    a = ao(s)
    t0=time.time()
    a.quickSort()
    #tiempo=tiempo+(time.time()-t0)
    #comp=comp+a.getCont()
    print('Quick Sort:', b[z], time.time()-t0,a.getCont())

print('\n\n\n')
#print('MergeSort:')

tiempo=0
comp=0

for z in range(len(b)):
    #for i in range(30):
    s = lp.listaPelisNele(b[z])
    a = ao(s)
    t0=time.time()
    a.mergeSort(s)
    #tiempo=tiempo+(time.time()-t0)
    #comp=comp+a.getCont()
    print('Merge Sort: ',b[z], time.time()-t0, a.getCont())


