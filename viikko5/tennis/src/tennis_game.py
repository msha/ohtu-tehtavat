from player import Player
import enum

class Score(enum.Enum):
    Love = 0
    Fifteen = 1
    Thirty = 2
    Forty = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.players = [self.player1,self.player2]

    def won_point(self, player_name):
        for player in self.players:
            if player._name == player_name:
                player.win_point()

    def get_score(self):
        score_to_text = ""

        if self.player1.get_score() == self.player2.get_score():
            score_to_text = "Deuce"
            if(self.player1.get_score() < 4):
                score_to_text = Score(self.player1.get_score()).name + '-All'
                
        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            if(self.player1.get_score() > self.player2.get_score()+1):
                score_to_text = "Win for player1"
            elif(self.player2.get_score() > self.player1.get_score()+1):
                score_to_text = "Win for player2"
            elif(self.player1.get_score()>self.player2.get_score()):
                score_to_text = "Advantage player1"
            else: 
                score_to_text = "Advantage player2"
        else:
                score_to_text += Score(self.players[0].get_score()).name+'-'+Score(self.players[1].get_score()).name

        return score_to_text
