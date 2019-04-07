import chess

ENGINE_PATH = '/usr/games/stockfish'


class Model:
    def __init__(self):
        self.board = chess.Board()
        self.num_players = int(input("Anzahl Spieler eingeben"))
        self.players = list()
        for x in range(self.num_players):
            name = input("Namen des {}. Spielers eingeben".format(x+1))
            self.players.append((name, 0))
        self.engine = chess.engine.SimpleEngine.popen_uci(ENGINE_PATH)
        self.halfmove_number = 0
        self.update_halfmove_number()

    def update_halfmove_number(self):
        turn = self.board.turn
        fullmoves = self.board.fullmove_number
        halfmoves = (fullmoves-1)*2             # -1 because fullmoves has offset + 1
        if not turn:
            # black to move
            halfmoves += 1
        self.halfmove_number = halfmoves

    def play(self):
        while not self.board.is_game_over():

            player_to_move = self.halfmove_number % self.num_players
            valid_move_inserted = False

            while not valid_move_inserted:
                move = input("{} am Zug. Bitte Zug eingeben.".format(self.players[player_to_move][0]))
                if move in list(map(lambda m: self.board.san(m), list(self.board.legal_moves))):
                    self.board.push_san(move)
                    valid_move_inserted = True
            print(self.board)
            self.update_halfmove_number()