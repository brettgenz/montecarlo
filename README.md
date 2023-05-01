Author: Brett Genz
Project: Monte Carlo Simulator

This module contains a Monte Carlo simulator consisting of three classes: <br>
- a Die class for creating dice with parameters for specifying faces and weights
- a Game class which rolls the dice a specified number of times 
- an Analyzer class which takes the results of a single game and computes various statistical properties about it.

=== Installing the Module ===

To install the module, at the command line or in a Jupyter notebook use the command:
!pip install -e .

=== Import Classes === 

from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

=== Creating a Die Object ===

faces = [1, 2, 3, 4, 5, 6]  # Specify the number and name of faces to be use on the die.

my_die = Die(faces)         # Create an instance of a Die.


=== Creating a Game Object ===

my_game = Game([my_die, my_die, my_die, my_die])  # Create a game with a list of 4 of my_die objects.

my_game.play(1000)     # Roll all 4 dice 1000 times each.


=== Creating an Analyzer Object ===

my_analyzer = Analyzer(my_game)  # Create an Analyzer object.

my_analyzer.jackpot()  # Compute how many times all dice rolled identical faces. This method stores the results as 
                       # a dataframe in a public attribute.

my_analyzer.combo()    # Compute the distinct combinations of faces along with their counts. This method stores the 
                       # results as a dataframe in a public attribute.
                       
my_analyzer.face_counts_per_roll()  # Compute how many times a given face is rolled in each event. This method
                                    # stores the results as a dataframe in a public attribute.
