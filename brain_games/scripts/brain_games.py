#!/usr/bin/env
from brain_games.cli import greet_and_get_name
from brain_games.shell import run_game
from brain_games.games import (
    brain_even, brain_calc, brain_gcd, brain_progression, brain_prime,
)


def main():
    greet_and_get_name()


def play_even():
    run_game(brain_even)


def play_prime():
    run_game(brain_prime)


def play_calc():
    run_game(brain_calc)


def play_gcd():
    run_game(brain_gcd)


def play_progression():
    run_game(brain_progression)


if __name__ == '__main__':
    main()
