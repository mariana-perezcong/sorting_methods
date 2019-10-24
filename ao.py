__author__ = 'mperezcs'
__author__ = 'mperezcs'

class ao:
    __datos=[]
    __cont=0

    def __init__(self, datos):
        self.__datos=datos
        self.__cont=0

    def getCont(self):
        return int(self.__cont)

    def getDatos(self):
        return self.__datos

    def swap(self, i, j):
        aux=self.__datos[i]
        self.__datos[i]=self.__datos[j]
        self.__datos[j]=aux

    def getDatos(self):
        return self.__datos

    def selectionSort(self):
        min=self.__datos[0]
        for i in range(len(self.__datos)):
            self.__cont=self.__cont+1
            j=i+1
            for j in range(len(self.__datos)):
                self.__cont=self.__cont+1
                if(self.__datos[j]>self.__datos[i]):
                    self.__cont=self.__cont+1
                    min=self.__datos[j]
                    aux=self.__datos[i]
                    self.__datos[i]=self.__datos[j]
                    self.__datos[j]=aux
        return self.__datos

    def bubbleSort(self):
        for i in range(len(self.__datos)):
            self.__cont=self.__cont+1
            r=len(self.__datos)-(i+1)
            for j in (range(r)):
                if(self.__datos[j]>self.__datos[j+1]):
                    self.__cont=self.__cont+1
                    aux=self.__datos[j]
                    self.__datos[j]=self.__datos[j+1]
                    self.__datos[j+1]=aux
        return self.__datos

    def insertionSort(self):
        for i in range(len(self.__datos)):
            j=i
            self.__cont=self.__cont+1
            while j>0 and self.__datos[j]<self.__datos[j-1]:
                self.__cont=self.__cont+1
                aux=self.__datos[j]
                self.__datos[j]=self.__datos[j-1]
                self.__datos[j-1]=aux
                j=j-1
        return self.__datos

    def quickSort(self):
        p=len(self.__datos)-1
        return self.quickSortR(0,p)

    def quickSortR(self, min, max):
        self.__cont=self.__cont+1
        if(min>max):
            return
        else:
            indice=self.part(min,max)
            self.quickSortR(min, indice-1)
            self.quickSortR(indice+1, max)
        return self.__datos

    def part(self, min,max):
        pivote=min
        gerardo=0
        i=min+1
        j=0
        while gerardo<(max-min):
            self.__cont=self.__cont+1
            if self.__datos[pivote]>= self.__datos[i]:
                self.__cont=self.__cont+1
                self.swap(pivote,i)
                gerardo=gerardo+1
                i=i+1
                pivote=pivote+1
            else:
                self.swap(i,max-j)
                j=j+1
                gerardo=gerardo+1
        return pivote

    def mergeSort(self,alist):
        if len(alist)>1:
            self.__cont=self.__cont+1
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                self.__cont=self.__cont+1
                if lefthalf[i] < righthalf[j]:
                    self.__cont=self.__cont+1
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                self.__cont=self.__cont+1
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                self.__cont=self.__cont+1
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
