import chess


class Model:
    def __init__(self):
        self.board = chess.Board()
        self.numPlayers = int(input("Anzahl Spieler eingeben"))
        self.players = list()
        for x in range(self.numPlayers):
            name = input("Namen des {}. Spielers eingeben".format(x+1))
            self.players.append((name, 0))
        print(self.players)