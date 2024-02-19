#!/usr/bin/env
from brain_games.cli import greet_and_get_name
from brain_games.shell import run_game
from brain_games.games import (
    brain_even, brain_calc, brain_gcd, brain_progression, brain_prime,
)


def main():
    greet_and_get_name()


if __name__ == '__main__':
    main()


def play_brain_even():
    run_game(brain_even)


def play_brain_calc():
    run_game(brain_calc)


def play_brain_gcd():
    run_game(brain_gcd)


def play_brain_progression():
    run_game(brain_progression)


def play_brain_prime():
    run_game(brain_prime)
