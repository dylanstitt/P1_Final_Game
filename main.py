from World import *
from Player import *
from art import *
import os


def playAgain():
    again = input('The game is over. Do you want to play the game again (y/n): ').lower()

    while again not in ['y', 'n']:
        again = input('Invalid response. Do you want to play the game again (y/n): ').lower()

    os.system('cls')
    if again == 'y':
        main()

    else:
        print(goodbye)


def main():
    world = World()
    player = Player(input('Enter the name for your character: '))

    start()

    playing = True
    while playing:
        os.system('cls')
        playing = player.move(world)

        if playing == 'Won Boss' or playing == 'Lost Fight' or playing == False:
            playing = False
            playAgain()

        elif playing == 'Won Fight':
            playing = True


if __name__ == '__main__':
    main()
