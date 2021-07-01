from numpy.random import randint
class Coin : 
   __value = ''
   

   def flip_coin(self)->None:
       sample_sp = ["malik","ketapah"]
       self.__value = sample_sp[randint(0,2)]
   def flip_value(self):
        return self.__value
    

   
    