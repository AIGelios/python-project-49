#!/usr/bin/env
import brain_games.cli as cli
from brain_games.shell import game_shell as run

import brain_games.games.brain_even as brain_even
import brain_games.games.brain_gcd as brain_gcd
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_prime as brain_prime
import brain_games.games.brain_progression as brain_prog


def welcome():
    print('Welcome to the Brain Games!')


def main():
    welcome()
    user = cli.username()
    cli.welcome_user(user)


def play_even():
    run(brain_even)


def play_prime():
    run(brain_prime)


def play_calc():
    run(brain_calc)


def play_gcd():
    run(brain_gcd)


def play_prog():
    run(brain_prog)


if __name__ == '__main__':
    main()
