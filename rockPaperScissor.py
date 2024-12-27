import random, sys

print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0


print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

while True:
    print('Wins ' + str(wins) + ', Losses ' + str(losses) + ', Ties ' + str(ties))
    while True:
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')

    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')
    
    computerMove = random.randint(1, 3)
    if computerMove == 1:
        computerMove = 'r'
        print('Rock')
    elif computerMove == 2:
        computerMove = 'p'
        print('Paper')
    elif computerMove == 3:
        computerMove = 's'
        print('Scissors')

    if playerMove == computerMove: 
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
    