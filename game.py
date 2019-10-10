import random

while(True): 
    user_choice = input('Choose rock (r), paper (p) or scissors (s): ')

    if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
        print(f'you chose "{user_choice}"')
        break
    else:
        print('Invalid input. Please enter the correct input.')

computer_choice_list = ['r','p','s']
computer_choice = random.choice(computer_choice_list)
print(f'the computer chose "{computer_choice}"')

if user_choice == computer_choice:
    print("It's a tie.")
elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
    print(f'You win! {user_choice} beats {computer_choice}')
else:
    print(f'You lose! {computer_choice} beats {user_choice}')