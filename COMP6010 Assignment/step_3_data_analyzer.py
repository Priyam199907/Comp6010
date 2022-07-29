'''
DO NOT REMOVE THIS COMMENT
STUDENT ID: 46291431
STUDENT NAME: Priyam Nikhil Padiya
[x]: add an 'x' inside the square brackets to declare that 
you haven't seen any other person's code
and you haven't shared your code with, or shown your code to, anyone
'''
import step_1_data_reader
import step_2_data_cleaner
import unittest

def get_average_rating(dict):			  				  		 	  	    		 	
    '''			  				  		 	  	    		 	
    Get a dictionary of the average critic ratings
    for each character in the dictionary
    '''			  				  		 	  	    		 	
    for key,values in dict.items():
        sum=0
        for i in values:
            sum+=i
        dict[key] = sum/len(values)
    return dict

class Tester(unittest.TestCase):
    def test_get_average_rating(self):			  				  		 	  	    		 	
        avatar = step_1_data_reader.read_data("avatar.csv")
        avatar_clean = step_2_data_cleaner.remove_lowest_highest(avatar)
        avatar_averages = get_average_rating(avatar_clean)
        avatar_actual = list(avatar_averages.values())
        avatar_expected = [6.33, 4.83, 5.67, 6.83, 7.83]
        for i in range(len(avatar_expected)):
            self.assertAlmostEqual(avatar_expected[i], avatar_actual[i], 1)

        harryPotter = step_1_data_reader.read_data("harryPotter.csv")
        harryPotter_clean = step_2_data_cleaner.remove_lowest_highest(harryPotter)
        harryPotter_averages = get_average_rating(harryPotter_clean)
        harryPotter_actual = list(harryPotter_averages.values())
        harryPotter_expected = [8.67, 8.33, 8.67, 8.67, 9.33, 8.0, 8.67, 6.67, 10.0, 8.0, 5.0, 6.0, 6.0, 6.33, 6.0]
        print(harryPotter_actual)
        for i in range(len(harryPotter_expected)):
            self.assertAlmostEqual(harryPotter_expected[i], harryPotter_actual[i], 1)

if __name__ == '__main__':
    unittest.main()


