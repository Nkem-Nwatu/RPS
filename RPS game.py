#note
# ctrl + ] for indenting

import random
def rps():
    keep_playing = True
    while keep_playing is True:
        I_play = input('Enter r for Rock, p for Paper or s for Scissors: ') #enter r or p or s
        possible_entries = ['r','p','s'] #choose from these
        computer_plays = random.choice(possible_entries) #computer randomly chooses

#two ways of printing out player's choice
# print('I played ' + str(I_play) + '; Computer played ' + str(computer_plays))
# or
        print(f'I played {I_play} and the Computer played {computer_plays}')

#what happens when I and Computers plays same game
        if I_play == computer_plays:
            print(f'Both players chose {I_play}; A tie!')

#what happens when i play rock and computer plays different
        elif I_play == 'r':
            if computer_plays == 's':
                print('rock smashes scissors, I win!')
            else:
                print('paper covers rock, Computer wins!')

#what happens when i play Paper and computer plays different.
        elif I_play == 'p':
            if computer_plays == 'r':
                print('paper covers rock, I win!')
            else:
                print('scissors cuts paper, Computer wins!')

#what happens when i play scissors and computer plays different.                
        elif I_play == 's':
            if computer_plays == 'p':
                print('scissors cuts paper, I win!')
            else:
                print('rock smashes scissors, Computer wins!')
        choice = input('Would you like to keep playing? [y/n]')
        if choice == 'y':
            keep_playing = True
        elif choice == 'n':
            keep_playing = False
        else:
            keep_playing = input('Would you like to keep playing? [y/n]')
                
rps()