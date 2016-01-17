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
