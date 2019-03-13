'''
A game in which the player has a limited 
number of tries to guess a secret number
'''

# --------------Guessing Game-------------- #

import random


def main():

    # Adjust game difficulty settings here
    guessing_game(
        n_min = 1,
        n_max = 20,
        turns = 3
    )


def guessing_game(n_min: int = 1, n_max: int = 10, turns: int = 3):

    try:
        if num_check((n_min, n_max, turns)) == True:
            secret_number = random.randint(n_min, n_max)
            print(f'Guess the secret number in {turns} turns or less!')
            input_loop(turns, secret_number)
    except ValueError as err:
        print('Game failed to start: all arguments must be of type integer.')
        return err
    else:
        print('Game Over')


def input_loop(t, s):

    for i in range(1, t + 1):
        print(f'Turn: {i}')

        if i == 5: 
            print('Last chance!')

        guess = int(input('Guess the secret number: '))
        
        if guess == s:
            print('You got it!')
            break
        elif guess == s + 1 or guess == s - 1:
            print('So close!')
        elif guess < s:
            print('Too low!')
        else:
            print('Too high')


def num_check(ls):
    check = all(isinstance(x, int) for x in ls)
    return check


if __name__ == '__main__':
    main()