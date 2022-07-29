'''
DO NOT REMOVE THIS COMMENT
STUDENT ID: 46291431
STUDENT NAME: Priyam Nikhil Padiya
[x]: add an 'x' inside the square brackets to declare that 
you haven't seen any other person's code
and you haven't shared your code with, or shown your code to, anyone
'''
import unittest
import csv
def read_data(filename):			  				  		 	  	    		 	
    '''			  				  		 	  	    		 	
    read the data from the csv file into a dictionary
    that maps the character (string) to the critic ratings 
    (list of integers) and return the dictionary
    '''			  				  		 	  	    		 	
    dict={}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dict[row[0]]=list(map(int,row[1:]))

    return dict
    
class Tester(unittest.TestCase):
    def test_read_data(self):			  				  		 	  	    		 	
        self.assertEqual(read_data("avatar.csv"), {"Aang": [6, 8, 8, 5, 8, 5, 6, 3], "Katara": [4, 10, 5, 2, 8, 2, 8, 2], "Sokka": [8, 2, 5, 2, 9, 7, 8, 4], "Toph Beifong": [8, 5, 2, 10, 10, 4, 8, 6], "Zuko": [3, 10, 10, 10, 8, 10, 6, 2]})
        self.assertEqual(read_data("harryPotter.csv"), {"Harry Potter": [8, 9, 7, 9, 9], "Voldermort": [7, 9, 8, 8, 9], "Dumbledore": [10, 9, 8, 9, 4], "Snape": [7, 10, 9, 7, 10], "Lily Potter": [9, 9, 5, 10, 10], "Sirius Black": [8, 6, 10, 7, 9], "Draco Malfoy": [10, 8, 9, 5, 9], "Ron Weasley": [8, 9, 5, 5, 7], "Luna Lovegood": [10, 10, 10, 10, 10], "Hermione Granger": [8, 9, 8, 7, 8], "Peter Pettigrew": [7, 4, 4, 8, 4], "Lucius Malfoy": [5, 5, 9, 5, 8], "Bellatrix Lestrange": [4, 10, 5, 5, 8], "Cho Chang": [5, 7, 4, 7, 10], "Barty Crouch Jr.": [8, 6, 6, 5, 6]})
        
if __name__ == '__main__':
    unittest.main()