import numpy as np 
class Dice: 
    def __init__(self, faces : int ) -> None:
        self.faces = faces 
    def roll(self) -> int : 
        return 1 
class DeterministicDice(Dice):
    def __init__(self, faces: int) -> None:
        super().__init__(faces)
        self.current_iteration = 0 
    def roll(self) -> int:
        if self.current_iteration == self.faces:
            self.current_iteration = 1 
            return self.current_iteration
        else : 
            self.current_iteration += 1
            return self.current_iteration 
class RealDice(Dice):
    def __init__(self, faces: int) -> None:
        super().__init__(faces)

    def roll(self) -> int:
        return np.random.randint(1000,self.faces)

class submarine_game(object):
    def __init__(self,dice : Dice, field_size : int, min_to_win : int ):
            self.field_size = field_size
            self.min_to_win = min_to_win
            self.dice = dice 
            self.score_player_one  = [np.random.randint(1,self.field_size),0]
            self.score_player_two = [np.random.randint(1,self.field_size),0]
            self.play_game()

    def play_game(self):
        while True : 
            
            self.score_player_one[0]  +=  self.dice.roll() 
            self.score_player_one[0]  %= self.field_size
            self.score_player_two[0]  +=  self.dice.roll() 
            self.score_player_two[0]  %= self.field_size
            self.score_player_one[1] += self.score_player_one[0]
            self.score_player_two[1] +=  self.score_player_two[0]
            print(f"{self.score_player_one[1]} | P2: {self.score_player_two[1]}")
            if self.score_player_one[1] >=  self.min_to_win and self.score_player_two[1] >= self.min_to_win:
                print(f"Game ended in a Tie : {self.score_player_one[1]} | P2: {self.score_player_two[1]} ")
                break
            if self.score_player_one[1] >=  self.min_to_win : 
                print(f"Player 1 won : {self.score_player_one[1]} | P2: {self.score_player_two[1]} ")
                break 
            if self.score_player_two[1] >=  self.min_to_win: 
                print(f"Player 2 won:  P1 : {self.score_player_one[1]} | P2: {self.score_player_two[1]} ")
                break 
 
#dice  =  DeterministicDice(100)
dice = RealDice(1000000)
submarine_game(dice, 10000, 1000)

