import unittest
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class MonteCarloTestSuite(unittest.TestCase):

    def test_1_create_die(self):
        """
        This method tests that an instance has been created and includes the correct number of faces.
        """
        # create instance
        
        n = 6
        
        test_die = Die(list(range(1, n + 1)))
        
        test_value = (len(test_die.die_df.faces) == n)
        
        message = "Error: Incorrect value for number of faces."
        
        self.assertTrue(test_value, message)

        
    def test_2_change_weights(self):
        """
        This method tests whether or not the change_weight() method correctly updated the weight of the specified face.
        """
        # create instance
        
        n = 6
        
        test_die = Die(list(range(1, n + 1)))
        
        test_die.change_weights(n, 5)
        
        test_value = test_die.die_df.weights[n - 1] == 5
        
        message = "Error: Incorrect weight for specified face."
        
        self.assertTrue(test_value, message)
        
        
    def test_3_roll_die(self):
        """
        This method tests whether or not the roll_die() method returns the correct number of rolls.
        """
        # create instance
        
        n = 6
        
        test_die = Die(list(range(1, n + 1)))
        
        test_value = len(test_die.roll_die(n)) == n

        message = "Error: Incorrect number of rolls."
        
        self.assertTrue(test_value, message)
    
    
    def test_4_show_die(self):
        """
        This method tests whether or not the private data frame self.die_df has the correct dimensions.
        """
        # create instance
        
        n = 6
        
        test_die = Die(list(range(1, n + 1)))
        
        test_value = test_die.show_die().shape == (n, 2)
        
        message = "Error: Incorrect dimensions of self.die_df."
        
        self.assertTrue(test_value, message)
        
        
    def test_5_play(self):
        """
        This method tests whether the play method creates a last_play data frame
        with the correct number of columns (dice) and rows (number of rolls).
        """
        # create instances of dice
        
        n = 6
        
        test_die_1 = Die(list(range(1, n + 1)))
        test_die_2 = Die(list(range(1, n + 1)))
        test_die_3 = Die(list(range(1, n + 1)))
        
        test_dice_list = [test_die_1, test_die_2, test_die_3]
        
        # create instance of game
        
        test_game = Game(test_dice_list)
        
        test_game.play(4)
        
        test_value = test_game.last_play.shape == (4, 3)
        
        message = "Error: Incorrect dimensions of test_game.last_play data frame."
        
        self.assertTrue(test_value, message)
        
        
    def test_6_show_last_play(self):
        """
        This method tests whether the show_last_play() method with the default parameter
        correctly returns the last_play object in wide format.
        """
        # create instances of dice
        
        n = 6
        
        test_die_1 = Die(list(range(1, n + 1)))
        test_die_2 = Die(list(range(1, n + 1)))
        test_die_3 = Die(list(range(1, n + 1)))
        
        test_dice_list = [test_die_1, test_die_2, test_die_3]
        
        # create instance of game
        
        test_game = Game(test_dice_list)
        
        test_game.play(4)
        
        test_game.show_last_play()
        
        test_value = test_game.last_play.shape == (4, 3)
        
        message = "Error: test_game.last_play data frame did not display in wide format."
        
        self.assertTrue(test_value, message)
        
        
    def test_7_jackpot(self):
        """
        This method tests whether the jackpot() method correctly counts the number of jackpots
        in the last_play results. For this method, all dice have identical faces so that all 
        rows of last_play will be jackpots. The number of jackpots should then equal the number 
        of rolls.
        """
        # create instances of dice with all identical faces 
        
        faces = [6,6,6,6,6,6]
        
        test_die_1 = Die(faces)
        test_die_2 = Die(faces)
        test_die_3 = Die(faces)
        
        test_dice_list = [test_die_1, test_die_2, test_die_3]
        
        # create instance of game
        
        test_game = Game(test_dice_list)
        
        test_game.play(4)
        
        test_analyzer = Analyzer(test_game)
        
        test_value = test_analyzer.jackpot() == 4
        
        message = "Error: test_game.last_play data frame did not display in wide format."
        
        self.assertTrue(test_value, message)
        
        
        
    def test_8_combo(self):
        """
        This method tests whether the combo() method correctly groups and counts matches
        from the game.last_play data frame. Each die has a single face, so every row will
        have the same combo, and the count of the 
        """
        # create instances of dice
        
        test_die_1 = Die(list('U'))
        test_die_2 = Die(list('V'))
        test_die_3 = Die(list('A'))
        
        test_dice_list = [test_die_1, test_die_2, test_die_3]
        
        # create instance of game
        
        test_game = Game(test_dice_list)
        
        test_game.play(4)
        
        test_analyzer = Analyzer(test_game)
        
        test_analyzer.combo()
        
        test_value = (test_analyzer.combos.index[0] == ['U','V','A']) & (test_analyzer.combos['count'][0] == 4)
    
        message = "Error: Incorrect values for the combo and count."
        
        self.assertTrue(test_value, message)
        
        
        
    def test_9_face_counts_per_roll(self):
        """
        This method tests whether the face_counts data frame has the correct shape given 
        the number of dice and rolls.
        """
        # create instances of dice
        
        n = 6
        
        test_die_1 = Die(list(range(1, n + 1)))
        test_die_2 = Die(list(range(1, n + 1)))
        test_die_3 = Die(list(range(1, n + 1)))
        
        test_dice_list = [test_die_1, test_die_2, test_die_3]
        
        # create instance of game
        
        test_game = Game(test_dice_list)
        
        test_game.play(4)
        
        test_analyzer = Analyzer(test_game)
        
        test_analyzer.face_counts_per_roll()
        
        test_value = test_analyzer.face_counts.shape == (4, 6)
        
        message = "Error: Incorrect dimensions for the face_counts data frame."
        
        self.assertTrue(test_value, message)
        
        
        
if __name__ == '__main__':

    unittest.main(verbosity=3)