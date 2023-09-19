import prompt

def welcome_user():
    '''Asking user's name and printing greeting'''
    global username
    username = prompt.string('GAME: May i have your name?\n\nYOU: ').capitalize()
    print(f'\nGAME: Hello, {username}!\n')
