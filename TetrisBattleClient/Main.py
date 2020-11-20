from TetrisBattleClient.GameClient import GameClient
import random
import logging

from TetrisBattleClient.internals.TetrisAction import TetrisAction
from TetrisBattleClient.internals.Board import Board
from TetrisBattleClient import Element

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)


def turn(gcb: Board) -> TetrisAction:
    # Код писать сюда!!!
    return random.choice(list(TetrisAction))


def main():
    gcb = GameClient(
        "http://codebattle2020.westeurope.cloudapp.azure.com/codenjoy-contest/board/player/74mk55p4yeec4oakbrxd?code=1580349968077581689&gameName=tetris")
    gcb.run(turn)


if __name__ == '__main__':
    main()
