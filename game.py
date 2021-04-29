import random


def start():
    num = int(random.randint(1, 11))
    print(num)
    print('Hi!')
    start = input('Do you want to play? (yes/no): ')
    tries = 5
    while start.lower() == 'yes':
        guess = int(input('Guess the number between 1 and 10: '))
        if guess == num:
            print('Congratulations')
            tries -= 1
            print(f'it took you {5 - tries} tries')
            play_again = input('Do yuo want to paly again? (yes/no): ')
            tries = 5
            num = int(random.randint(1, 11))
            if play_again.lower() == 'no':
                print('ok, bye')
                break
        elif guess > num:
            print('guess number is lower than you have typed')
            tries -= 1
            print(f'you have {tries} tries left')
        elif guess < num:
            print('guess number is higher than you have typed')
            tries -= 1
            print(f'you have {tries} tries left')
        if tries == 0:
            print('You loose')
            break


start()
