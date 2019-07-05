import random

while True:
    print('Make your choice.')
    choice = str(input())
    choice = choice.lower()
    
    print("My choice is", choice)
    
    choices = ['rock', 'paper', 'scissors']
    
    computer_choice = random.choice(choices)
    
    print('Computer choice is', computer_choice)
    if choice in choices:
        if choice == computer_choice:
            print('It is a tie.')
        if choice == 'rock':
            if computer_choice == 'paper':
                print('you lose, sorry :(')
            elif computer_choice == 'scissors':
                print('you won, congrats :)')
        if choice == 'paper':
            if computer_choice == 'scissors':
                print('you lose, sorry :(')
            elif computer_choice == 'rock':
                print('you won, congrats :)')
        if choice == 'scissors':
            if computer_choice == 'rock':
                print('you lose, sorry :(')
            elif computer_choice == 'paper':
                print('you won, congrats :)')
    else:
        print('invalid choice, try again')
        
    print()