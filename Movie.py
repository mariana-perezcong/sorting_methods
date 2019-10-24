__author__ = 'mperezcs'

class Movie:
   __id=0
   __name=0
   __year=0

   def __init__(self,id, year,name):
       self.__id=id
       self.__year=year
       self.__name=name
   def getId(self):
       return self.__id

   def getName(self):
       return self.__name

   def getYear(self):
       return self.__year

   def __str__(self):
       return self.__id,self.__year, self.__name

   def __eq__(self,other):
       if self.__id==other.getId():
           return True
       else:
           return False
   def __le__(self,other):
       if self.__id<=other.getId():
           return True
       else:
           return False
   def __lt__(self, other):
       if self.__id<other.getId():
           return True
       else:
           return False
   def __ge__(self,other):
       if self.__id>=other.getId():
           return True
       else:
           return False

   def __gt__(self, other):
       if self.__id>other.getId():
           return True
       else:
           return False
