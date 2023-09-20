#!/usr/bin/env
import brain_games.cli as cli


def welcome():
    print('Welcome to the Brain Games!')


def main():
    welcome()
    user = cli.username()
    cli.welcome_user(user)


if __name__ == '__main__':
    main()
