import random

computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
user_choice = input('Do You Want - Rock, Paper, or Scissors?\n')

if computer_choice == user_choice:
    print('Tie')

elif user_choice == 'Rock' and computer_choice == 'Scissors':
    print('Win, The Computer Had ' + computer_choice)

elif user_choice == 'Paper' and computer_choice == 'Rock':
    print('Win, The Computer Had ' + computer_choice)

elif user_choice == 'Scissors' and computer_choice == 'Paper':
    print('Win, The Computer Had ' + computer_choice)

else:
    print('You Lose, The Computer Wins. The Computer Had ' + computer_choice)

