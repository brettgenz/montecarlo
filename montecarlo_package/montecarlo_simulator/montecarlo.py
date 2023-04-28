import pandas as pd
import numpy as np


class Die():
    """
    A die has N sides, or "faces", and W weights, and can be rolled to select a face.
    
    Methods:
        - roll_die
        - change_weight
        - show_die
    
    """
    
    def __init__(self, faces):
        """
        This method takes a list of values that will become the faces on the die. Values in
        the list can be characters or integers. The method initializes the weight of each
        face as 1. The method saves the faces and weights in a private data frame that can
        be used by other methods.
        """
        self.faces = faces # might want to do sort(faces) here
        if not isinstance(self.faces, list):
            raise ValueError("You must input a list of values.")
    
        x = [type(x) == str or type(x) == int for x in self.faces]
        
        if False in x:
            raise ValueError("All elements of the list must be characters or integers.")
    
        self.die_df = pd.DataFrame({
            "faces": faces,
            "weights": [1 for x in faces]
        })
        
        self.faces_type_list = list(set([type(x) for x in self.faces]))
        
    
    def change_weights(self, face, new_weight):
        """
        This method updates the weight of a single face of a die. It takes as input an 
        existing face on a die and a new weight (as a float). For validation, it checks
        whether the face exists on the die, and whether the new weight is a float or 
        can be coerced to a float. The method then finds the index of the face in self.faces,
        and sets the weight for the corresponding index in weights to the new weight.
        """
        if face not in self.faces:
            raise ValueError("The given face does not exist on this die.")
        
        if not type(float(new_weight)) == float:
            raise ValueError("The new weight must be a number.")
        
        index = self.die_df.faces.index[self.die_df.faces == face][0]
        
        self.die_df.weights[index] = new_weight
        
    
    def roll_die(self, n_rolls=1):
        """
        This method rolls the instantiated die a number of times equal to the supplied
        parameter n_rolls, and returns a pandas series of the results of the roll(s).
        """
        
        results = []
        
        for i in range(n_rolls):
            result = self.die_df.faces.sample(weights = self.die_df.weights).values[0]
            results.append(result)
        
        self.results = pd.Series(results)
        
        return results

    
    def show_die(self):
        """
        This method returns the current state of the data frame of the faces and weights
        of the die.
        """
        return self.die_df
    
class Game():
    """
    A game consists of rolling one or more dice of the same kind one or more times. Each 
    die in a given game must have the same number of sides and associated faces, but each die 
    object may have its own weights. 
    
    The class has one behavior: to play the game, which means roll all the dice a given 
    number of times.
    
    The class stores the results of its most recent play in a private data frame.
    """
    
    def __init__(self, dice):
        """
        This initializer takes one parameter: a list of already-instantiated similar Die
        objects. 
        
        The initializer tests:
        - whether the object passed is a list
        - whether each object in the list is a Die object
        - whether all dice have the same set of faces
        
        Finally, the initializer stores the list of face types for the first Die for later
        use by the Analyzer class.
        """
        
        self.dice = dice
        
        if not isinstance(self.dice, list):
            raise ValueError("You must input a list of existing Die objects.")
        
        x = [type(x) == Die for x in self.dice]
        
        if False in x:
            raise ValueError("All elements of the list must be existing Die objects.")
        
        # check whether all dice in self.dice have the same faces
        
        for i in range(1, len(self.dice)):
            if not dice[0].faces.sort() == dice[i].faces.sort():
                raise ValueError("All dice in the game must have the same faces.")
        
    
    
    def play(self, n):
        """
        This method takes a parameter for how many times the dice should be rolled.
        
        The class then saves the result of the play to a private data frame of shape N 
        rolls by M dice. The data frame uses the roll number as a named indec.
        
        The resulting data frame has columns for the roll number, the die number (its
        list index), and the face rolled in that instance.
        
        roll_number |  0  |  1  |  2  |  .  |  .  |  m  |
        -------------------------------------------------
             0      |  4  |  2  |  3  |  .  |  .  |  1  |
             1      |  1  |  5  |  2  |  .  |  .  |  2  |
             2      |  3  |  4  |  6  |  .  |  .  |  1  |
             .      |  .  |  .  |  .  |  .  |  .  |  5  |
             .      |  .  |  .  |  .  |  .  |  .  |  3  |
             n      |  6  |  1  |  5  |  4  |  2  |  6  |
        
        """
        
        self.last_play = pd.DataFrame(columns = [x for x in range(len(self.dice))],
                                      index = [x for x in range(n)])
        
        self.last_play.index.name = 'roll_number'
        
        for i in self.last_play.columns:
            self.last_play[i] = self.dice[i].roll_die(n)
        
        
    def show_last_play(self, nw_form=0):
        """
        This method simply the data frame with the results of the last play. It includes an
        additional parameter to allow a user to return the data frame in either wide (nw_form=0) 
        or narrow (nw_form=1) form.
        """
        
        if not (nw_form == 0 or nw_form == 1):
            raise ValueError("Enter 0 to return the last play in wide form or 1 to return it in narrow form.")
        
        if nw_form == 0:
            return self.last_play
        
        if nw_form == 1:
            return self.last_play.unstack()
        
        
class Analyzer():
    """
    This class takes as input the results of a single game and computes various descriptive
    statistical properties about it. These properties results are available as attributes
    of an Analyzer object.
    
    Methods:
      - jackpot
      - combo
      - face_counts_per_roll
    
    """
    
    def __init__(self, game):
        """
        This initializer takes a game object as its input parameter. 
        
        At initialization, it makes note the data type of the first die in the game's dice 
        list. Note: the initializer for the Game checks whether the list of faces on all dice 
        are identical. Therefore, the initializer only needs to know the face types of one Die.
        """
        
        self.game = game
        
        self.game_face_types = self.game.dice[0].faces_type_list
        
    
    def jackpot(self):
        """
        This method computes how many times the game resulted in all faces being identical. It
        creates a new column that calculates the length of a set created by the other rows of 
        results, and gives this cell a value of 1 if the length of the set is 1, and 0 otherwise. 
        It returns the sum of this column.
        """
        
        length = self.game.last_play.shape[0] # number of rows
        
        self.game.last_play['jackpot'] = 0
        
        width = self.game.last_play.shape[1]
        
        for i in range(length):
            if len(set(self.game.last_play.iloc[i, 0:(width-1)])) == 1:
                self.game.last_play['jackpot'].iloc[i] = 1
        
        return sum(self.game.last_play['jackpot'])
        
        
        
    def combo(self):
        """
        This method computes the distinct combinations of faces rolled, along with their counts.
        
        The combinations are sorted and stored as a multi-columned index, and then saved as a
        data frame in a public attribute.
        """
        # extract all of the rows of last_play into a list of lists, convert 
        # the list to a pd.Series, then assign my_df = series.value_counts().to_frame()
        
        all_combos = pd.Series([list(self.game.last_play.iloc[x, 0:5]) for x in range(len(self.game.last_play.index))])
        
        self.combos = all_combos.value_counts().to_frame('count')
        
        self.combos.index.name = 'unique_combos'
        
        self.combos.sort_values(by = ['count'], ascending=False)
        
        
    def face_counts_per_roll(self):
        """
        This method computes how many times per roll a given face is rolled in each event. For 
        example, if a roll of 5 dice has all sixes, then the counts for that roll would be
        6 for the face value of '6' and 0 for the other faces.
        
        The method stores the results as a data frame in a public attribute. This data frame has
        an index of the roll number and the face values as columns (i.e., the data frame is in
        wide format).
        """
        
        length = self.game.last_play.shape[0] # number of rows
        
        self.face_counts = pd.DataFrame(
            columns = [self.game.dice[0].faces[x] for x in range(len(self.game.dice[0].faces))],
            index = [x for x in range(length)]
        )
        
        self.face_counts.index.name = 'roll_number'
        
        for column in list(self.face_counts.columns):
            for row in range(len(self.face_counts.index)):
                col_index = self.face_counts.columns.get_loc(column)
                self.face_counts.iloc[row,col_index] = list(self.game.last_play.iloc[row]).count(column)
        
        
