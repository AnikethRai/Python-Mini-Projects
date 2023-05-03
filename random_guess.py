import random
play = input('Do you wanna play the number guessing game?(Y/N) ')
if play.lower() == 'y' or play.lower() == 'yes':
    user = input('Please enter your name: ')
else:
    quit()

count = 1
stupidity_count = 0
r = int(input('Please enter the range of numbers you want to play: '))
random_number = random.randint(0,r)
print(f'\n\n Let us start guessing ! The guessing range is (0 -> {r}) \n\n')

print('*'*100)
while True:

    if count > 20:
            print(f'You have exceeded the guessing limit! \n The number was -> {random_number} <- \n Try the game again.')
            print('*'*100)
            print('Thanks for playing')
            print('*'*100)
            break
    user_guess = input(f'Guess {count} : Enter your number : ')
    if user_guess.isdigit():
        if int(user_guess) == random_number:
            print(f'Bingo the number is {random_number}')
            print('*'*100)
            print(f'Thank you for playing {user}!')
            print('*'*100)
            break
        elif int(user_guess) < random_number:
            count += 1
            if int(user_guess) < random_number and int(user_guess) > random_number - 5:
                print('Close enough but lesser ! there try again')
            else:
                print('Your guess is lower than the random number! Guess again')
            
        elif int(user_guess) > random_number:
            count += 1
            if int(user_guess) > random_number and int(user_guess) < random_number + 5:
                print('Close enough but higher')
            else:
                print('Your guess is higher than the random number! Guess again')
            
    elif stupidity_count > 5:
            print('You dumb you dont know what is a digit! Go study from play school ! Well try again.')
    elif not user_guess.isdigit():
        stupidity_count += 1
        print('Your input is not a digit! Try again you buffoon.')

if count == 1:
    print('You are an amazing guesser')
elif count == 19:
    print('Oh my you love gambling!')
elif count > 1:
    print(f'You took {count} times to guess! But good work!')
elif count > 15:
    print(f'Get Better!')
            

    