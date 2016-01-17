import unittest
from rover import Rover

class TestApiSetup(unittest.TestCase):
    """
    This class tests the basic setup process of the 'Rover Api'.
    I recently read about "purely functional state" in the book 
    "Funcitonal Programming in Scala" (https://www.manning.com/books/functional-programming-in-scala)
    and I want to use some of those concepts.
    I use python because I'm not yet as fluent in Scala :).
    
    The API will be exposed by an immutable object representing the current state of the rover.
    Calling methods that trigger a state-transition (e.g. movement, turning) will,
    instead of manipulating the internal representation, the methods will return a new
    state object representing the new state.
    """

    def test_create_normal(self):
        rover = Rover()
        self.assertIsInstance(rover, Rover)

    def test_default_setup(self):
        rover = Rover()
        self.assertEqual(rover.get_position(), (0,0))
        self.assertEqual(rover.get_orientation(), 'N')
        self.assertEqual(rover.get_width(), 5)
        self.assertEqual(rover.get_height(), 5)

    def test_custom_setup(self):
        rover = Rover(5, 5, 'S', 10, 10)
        self.assertEqual(rover.get_position(), (5,5))
        self.assertEqual(rover.get_orientation(), 'S')
        self.assertEqual(rover.get_width(), 10)
        self.assertEqual(rover.get_height(), 10)

    def test_illegal_setup(self):
        negative_x = lambda: Rover(-1, 0)
        negative_y = lambda: Rover(0, -1)
        negative_width = lambda: Rover(width = -1)
        negative_height = lambda: Rover(height = -1)
        wrong_orientation = lambda: Rover(orientation = 'G')
        self.assertRaises(ValueError, negative_x)
        self.assertRaises(ValueError, negative_y)
        self.assertRaises(ValueError, negative_width)
        self.assertRaises(ValueError, negative_height)
        self.assertRaises(ValueError, wrong_orientation)
        

if __name__ == '__main__':
    unittest.main()
