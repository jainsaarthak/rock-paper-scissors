user_choice = input('Choose rock (r), paper (p) or scissors (s):')
# todo run some validation, raise error or ask for input again in case of invalid input
print(f'you chose "{user_choice}"')

# todo: implement some logic for the computer choice
# starting with always rock
computer_choice = 'r'
print(f'the computer chose "{computer_choice}"')


# todo more clean an smart verification
# rock beats scissors
if user_choice == 'r':
    if computer_choice == 's':
        print('You Win! Rock beats scissor!')
    elif computer_choice == 'p':
        print('You lose! Paper beats rock!')
    elif computer_choice == 'r':
        print("It's a tie.")

# paper beats rock
if user_choice == 'p':
    if computer_choice == 'r':
        print('You Win! Paper beats rock!')
    elif computer_choice == 's':
        print('You lose! Scissors beats paper!')
    elif computer_choice == 'p':
        print("It's a tie.")

# scissors beats paper
if user_choice == 's':
    if computer_choice == 'p':
        print('You Win! Scissors beats paper!')
    elif computer_choice == 'r':
        print('You lose! Rock beats scissor!')
    elif computer_choice == 's':
        print("It's a tie.")
