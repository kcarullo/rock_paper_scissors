"""rock, paper, scissor without if statements"""
import random 
import time

while True:
    print('Rock, paper, scissors...shoot!(type rock, paper, or scissors)')
    time.sleep(1)
    choice = str(input())
    choice = choice.lower()
    print("My choice is", choice)
    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    print('Computer choice is', computer_choice)
    
    choice_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
    choice_index = choice_dict.get(choice, 3)
    computer_index = choice_dict.get(computer_choice)
    
    print('Choice index', choice_index)
    print('computer choice index', computer_index)
    
    result_matrix = [[0,2,1],
                     [1,0,2], 
                     [2,1,0], 
                     [3,3,3]]
    
    result_idx = result_matrix[choice_index][computer_index]
    result_messages = ['it is a tie', 'You win', 'Sorry, you lose :(', 'invalid choice, try again']
    result = result_messages[result_idx]
    print(result)
    print()
    
str()
