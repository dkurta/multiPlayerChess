import chess

ENGINE_PATH = '/usr/games/stockfish'
ENGINE_TIME_LIMIT = 0.100

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
            pre_rating = self.engine.analyse(self.board, chess.engine.Limit(time=ENGINE_TIME_LIMIT))

            player_to_move = self.halfmove_number % self.num_players
            move_for_white_side = self.board.turn
            valid_move_inserted = False
            while not valid_move_inserted:
                move = input("{} am Zug. Bitte Zug eingeben.".format(self.players[player_to_move][0]))
                if move in list(map(lambda m: self.board.san(m), list(self.board.legal_moves))):
                    self.board.push_san(move)
                    valid_move_inserted = True

            new_rating = self.engine.analyse(self.board, chess.engine.Limit(time=ENGINE_TIME_LIMIT))
            delta = calculate_delta(move_for_white_side, pre_rating['score'], new_rating['score'])
            pre_rating = new_rating
            self.players[player_to_move][1] += delta
            print(self.board)
            print(self.players)
            self.update_halfmove_number()


def calculate_delta(color, rating_before, rating_after):
    print(rating_before, rating_after)
    delta = rating_after - rating_before
    if not color:
        # moved for black
        print("Moved for black")
        delta = delta*(-1)
    return delta