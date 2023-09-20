#!/usr/bin/env
import brain_games.cli as cli


def welcome_to_the_game():
    print('Welcome to the Brain Games!')


def main():
    welcome_to_the_game()
    user = cli.username()
    cli.welcome_user(user)


if __name__ == '__main__':
    main()
