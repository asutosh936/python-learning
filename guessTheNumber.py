
print('I am thinking of a number between 1 and 20.')
print('Take a guess.')
number = 0

guess = 0

while(number <= 20):
    if(number < 16):
        guess = guess + 1
        print('Your guess is too low.')
        number = int(input())
        continue
    elif(number > 17):
        guess = guess + 1
        print('Your guess is too high.')
        number = int(input())
        continue
    elif(number == 16):
        print('Good job! You guessed my number on ' + str(guess) + ' guesses!')
        break


