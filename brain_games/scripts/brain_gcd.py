#!/usr/bin/env
from brain_games.shell import game_shell as run
import brain_games.games.gcd as game


def main():
    '''Run the game "Find the greatest common divisor"'''
    run(game)


if __name__ == '__main__':
    main()
