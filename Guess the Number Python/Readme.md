"""
"Guess the Number Python"
-------------------------
import the random module from python's inbuilt libraries

user inputs a number; a lower limit and an upper limit.

After getting the upper limit and the lower limit within which a random number will be selected, we pick a random number using a function from the random module.

The user is then assigned a number of chances to guess a number which will be a counter for a loop. We use a while loop since the user can get the right guess at any trial. The while case will check if the user has guessed the right number and if so, exits the loop. If not the number of chances decrements by one until the user has no more chances and the random number is revealed to him.

To ensure that the program runs continuously and doesn't close the program window, we add a true statement and print a line to separate the blocks.

Another method:
---------------
# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


"""