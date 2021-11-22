class PlayerStats:
    def __init__(self,reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self,nat):

        pelaajat = self.reader.get_players()

        palautus = []

        for player in pelaajat:
            if player.nationality == nat:
                palautus.append(player)
        
        palautus.sort(key=lambda p: p.points, reverse=True)
        
        return palautus
