Author: Brett Genz<br>
Project: Monte Carlo Simulator

This module contains a Monte Carlo simulator consisting of three classes: <br>
- a Die class for creating dice with parameters for specifying faces and weights
- a Game class which rolls the dice a specified number of times 
- an Analyzer class which takes the results of a single game and computes various statistical properties about it.

=== Installing the Module ===

To install the module, at the command line or in a Jupyter notebook use the command:<br>
!pip install -e .

=== Import Classes === 

from montecarlo import Die<br>
from montecarlo import Game<br>
from montecarlo import Analyzer<br>

=== Creating a Die Object ===

# Specify the number and name of faces to be use on the die.
faces = [1, 2, 3, 4, 5, 6]  

# Create an instance of a Die.
my_die = Die(faces)         


=== Creating a Game Object ===

# Create a game with a list of 4 of my_die objects.
my_game = Game([my_die, my_die, my_die, my_die])  

# Roll all 4 dice 1000 times each.
my_game.play(1000)     


=== Creating an Analyzer Object ===

# Create an Analyzer object.
my_analyzer = Analyzer(my_game)

# Compute how many times all dice rolled identical faces. This method stores the results as a dataframe in a public attribute.
my_analyzer.jackpot()   

# Compute the distinct combinations of faces along with their counts. This method stores the results as a dataframe in a public attribute.
my_analyzer.combo()    

# Compute how many times a given face is rolled in each event. This method stores the results as a dataframe in a public attribute.
my_analyzer.face_counts_per_roll()  
