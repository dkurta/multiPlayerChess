import chess
import chess.engine
from src import model

engine = chess.engine.SimpleEngine.popen_uci('/usr/games/stockfish')

# board = chess.Board()
# info = engine.analyse(board, chess.engine.Limit(time=4.100))
# print(info)
# print("score= ", info['score'])
# print(type(info['score']))





# engine.quit()

if __name__ == '__main__':
    model = model.Model()
    model.play()