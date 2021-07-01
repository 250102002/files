from Coin import Coin 
from Player import Player
from ScorBoard import ScoreBoard



class GameEngine : 
    __isGameRuning = False
    def is_game_runing(self):
        return self.__isGameRuning
    
    def get_player_num(self):
        try :
            num = int(input("Enter the players num(1,2,3) or (ctrl+c) for end the game : ").strip())
            if num > 3 or num < 0 :
                print("Enter a valid number..")
                self.get_player_num(GameEngine)
            return num
        except :
            print("Enter a valid number..")
            self.get_player_num(GameEngine)




    def compare(self,guess,obj):
        Coin.flip_coin(Coin)
        value= Coin.flip_value(Coin)
        
        if guess ==value :
            obj.increase()
        elif guess == "0":
            self.end_game(GameEngine,obj)




    def end_game(self,player1=None,player2=None,player3=None):
        winner_num,highscore = ScoreBoard.get_winner(ScoreBoard,player1=player1,player2= player2,player3 = player3)
        print("player",winner_num," is is the winner and his score is ",highscore)
        self.__isGameRuning == False




    def game(GameEngine,player1=None,player2=None,player3=None,num_of_players=0):
        guess = ''
        if num_of_players == 1 :
            guess = player1.guess()
            if player1.get_playerNum() == 0 :
                player1.set_number(1)
            
                
            GameEngine.compare(GameEngine,guess,player1)
            print("player"+str(player1.get_playerNum())+" is "+str(player1.get_score()))
            GameEngine.game(GameEngine,player1,num_of_players=num_of_players)
        elif num_of_players == 2 :


            for player in [player1,player2] :
                
                guess = player.guess()
                GameEngine.compare(GameEngine,guess,player)
            

            score1 = player1.get_score(); score2= player2.get_score() 
            for num,score in enumerate([score1,score2],start=1):
                ScoreBoard.show_score(ScoreBoard,score,num)
            
            GameEngine.game(GameEngine,player1,player2,num_of_players=num_of_players)


        elif num_of_players== 3 :

            for player in [player1,player2,player3]:
                if player.get_playerNum() == 0 :
                    player.set_number(3)
                guess = player.guess()
                GameEngine.compare(GameEngine,guess,player)
            score1 = player1.get_score(); score2= player2.get_score() ; score3= player3.get_score()
            for num,score in enumerate([score1,score2,score3],start=1):
                ScoreBoard.show_score(ScoreBoard,score,num)

            GameEngine.game(GameEngine,player1,player2,player3,num_of_players=num_of_players)


        else :
            GameEngine.end_game(GameEngine)






    @staticmethod
    def Start_game(self):
        self.__isGameRuning = True 
        global guess 
        guess = ''
        player1 = Player(1)
        player2 = Player(2)
        player3 = Player(3)
        while self.is_game_runing(GameEngine) :
            player_num = self.get_player_num(GameEngine)
            if player_num == 1 :
                player = Player(1)
                self.game(GameEngine,player1 = player,num_of_players =player_num)
            elif player_num == 2 :
                
                self.game(GameEngine,player1 = player1,player2 = player2,num_of_players =player_num)
            elif player_num == 3 :
                
                self.game(GameEngine,player1,player2,player3,num_of_players=player_num)
            else :
                self.game(GameEngine)



            
            
        
