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

The simplest I can figure is a console application.

* The user calls the game from the terminal
* The system shows three options (Rock, Paper and Scissors) and their respective keys
* The user press one of the keys and hits enter
* The game replies showing the user's choice, the computer's choice and the result of the game. The program ends.


# Take a slice with all layers of the cake

Once we have a rough idea what the system should do, we develop a "slice" of the cake that contains all the layers: that mean the game should provide a way for:

* the users to input their choice;
* define the computers choice
* process the "battle"
* output the result

Later in the [full code](#the-code), you can see how the complete first draft look like.

## Getting the users choice as input

I want the first draft to come out quickly. So I'm simplifying each layer in order to make them fit together. That means I will sacrifice some features of the user input. In this case, I'll use [Python's built in input](https://docs.python.org/3/library/functions.html#input) to and store the raw value into a variable. No validation is performed at this point.

``` python3
user_choice = input('Choose rock (r), paper (p) or scissors (s):')
# todo run some validation, raise error or ask for input again in case of invalid input
print(f'you chose "{user_choice}"')
```

What happens if the user inputs a letter that does not represent a game entity?
I **know** that some validation will be necessary. So I make a note that this feature is incomplete. This could be a new ticket, or and additional note on the input issue requirement.

After creating this part of the code I might want to provide the user input message in different languages. Or wish that the user doesn't need to press a key and then enter. Just the key related to the option.

All these new issues might appear before or later the first implementation. I consider all this as improvements. This should be evaluated with the customer to set priorities. After all, maybe the customers didn't even thought that they would be required to press the key and then enter. **It's OK not to know everything in advance**.


## Getting the computer's choice

What's the simplest thing that could possible work? In this case, I decided that a hardcoded value would be OK.

``` python3
# todo: implement some logic for the computer choice
# starting with always rock
computer_choice = 'r'
print(f'the computer chose "{computer_choice}"')
```

Thinking about a larger system, this could be an entire module, a database search, algorithm process and return of value that could take days or weeks to develop.
The nice thing with the *Fake it until you make it*, is that you can make a conscious choice of delaying work you know that has to be done. 

But what do you gain with that? 

You gain a view of the integration of the parts. 

Hopefully you will se more value in the parts that work together than the parts not yet implemented. You might even get valuable feedback from the customer even if the computer chooses only rock.


## The "battle" algorithm

Now that I managed to create a ridiculously simple way to get the user and the computer choices, I need to compare them and decide the winner.

My first objective was in understanding how the verification would work. 

``` python3
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

I ended with a lot of similar, copy-paste-edit-a-bit pieces of code. If this was a more complex game with 15 possibilities this would be an incredible bad solution. In such case I would limit the possibilities of input and output. Just to grasp the data structures and get a *feeling* of the solution algorithm.




## The code

Here's the implementation of the first version. Just one file. No functions. As ugly as it can be:

``` python3
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

