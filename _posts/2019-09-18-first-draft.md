---
layout: post
title:  "First Draft!"
author: Pedro Zamuner
published: true
---

# Do the simplest thing that could possibly work

Simplicity is important. Always. Specially in early stages of a Software Project. You might not know what your customer will think about your system; or customers might think they know what they need and start telling you the solution they want, instead of telling you about their problem; or you just want to tackle a problem, a new programming language or technology.

Start simple and make sure you get a better picture of the problem. Sometimes you have to write a bit of the solution to better understand the problem. You might need the customers to take a look on your solution to see if their problem is being solved.


## What do I want?

I want a simple game of Rock-Paper-Scissors. I want to lead you through the development of the system pointing out my discoveries, techniques and experience.


## How does the simplest version of the game look like?

The simples I can figure is a console application.

* The user calls the game from the terminal
* The system shows three options (Rock, Paper and Scissors) and their respective keys
* The user press one of the keys and hits enter
* The game replies showing the user choice, the computer's choice and the result of the game. The program ends.


# Take a slice with all layers of the cake

Once we have a rough idea what the system should do, we develop a "slice" of the cake that contains all the layers: that mean the game should provide a way for:

* the users to input their choice;
* define the computers choice
* process the "battle"
* output the result

Later in the [full code](#the-code) you can see how the first draft look like.

## Getting the users input

I want the first draft to come out quickly. 
...


## The code

Here's the implementation of the first version. Just one file. No functions. As ugly as it can be:

```python3
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
```

