'''
DO NOT REMOVE THIS COMMENT
STUDENT ID: 46291431
STUDENT NAME: Priyam Nikhil Padiya
[x]: add an 'x' inside the square brackets to declare that 
you haven't seen any other person's code
and you haven't shared your code with, or shown your code to, anyone
'''
import step_1_data_reader
import unittest

def remove_lowest_highest(dict):			  				  		 	  	    		 	
    '''			  				  		 	  	    		 	
    Remove the lowest and highest critic
    ratings for each character, and return the updated
    dictionary.
    For example, if the ratings for a character
    are [6, 2, 9, 5, 7], after the function executes,
    the ratings for the character should be [6, 5, 7]
    '''			  				  		 	  	    		 	
    for key,value in dict.items():
        value.remove(max(value))
        value.remove(min(value))
        dict[key]=value
    return dict

class Tester(unittest.TestCase):
    def test_remove_lowest_highest(self):			  				  		 	  	    		 	
        avatar = step_1_data_reader.read_data("avatar.csv")
        self.assertEqual(remove_lowest_highest(avatar), {'Aang': [6, 8, 5, 8, 5, 6],'Katara': [4, 5, 8, 2, 8, 2],'Sokka': [8, 5, 2, 7, 8, 4],'Toph Beifong': [8, 5, 10, 4, 8, 6],'Zuko': [3, 10, 10, 8, 10, 6]})
        
        harryPotter = step_1_data_reader.read_data("harryPotter.csv")
        self.assertEqual(remove_lowest_highest(harryPotter), {'Barty Crouch Jr.': [6, 6, 6],'Bellatrix Lestrange': [5, 5, 8],'Cho Chang': [5, 7, 7],'Draco Malfoy': [8, 9, 9],'Dumbledore': [9, 8, 9],'Harry Potter': [8, 9, 9],'Hermione Granger': [8, 8, 8],'Lily Potter': [9, 9, 10],'Lucius Malfoy': [5, 5, 8],'Luna Lovegood': [10, 10, 10],'Peter Pettigrew': [7, 4, 4],'Ron Weasley': [8, 5, 7],'Sirius Black': [8, 7, 9],'Snape': [9, 7, 10],'Voldermort': [8, 8, 9]})
        
if __name__ == '__main__':
    unittest.main()