


# from coin_guess_game.GameEngine import GameEngine


class Player :
    __score = 0
    __guess = ''
    
    def __init__(self,num) -> None:
        self.__number = num
    def guess(self):
        self.__guess = input("player"+str(self.__number)+" guess is : ").strip()
        if self.__guess.lower() not in ["malik","ketapah"]:
            print("Enter a valid guess from (malik,ketapah)... or Enter ctrl+c to end the game ..")
            self.guess()
        else :
            return self.__guess
    
           
       
            
            
            


    def increase(self):
        self.__score+= 1
    def set_number(self,number):
        self.__number = number
    def get_score(self):
        return self.__score
    def get_playerNum(self):
        return self.__number
    
    
