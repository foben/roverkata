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
        zero_width = lambda: Rover(width = 0)
        zero_height = lambda: Rover(height = 0)
        wrong_orientation = lambda: Rover(orientation = 'G')
        self.assertRaises(ValueError, negative_x)
        self.assertRaises(ValueError, negative_y)
        self.assertRaises(ValueError, negative_width)
        self.assertRaises(ValueError, negative_height)
        self.assertRaises(ValueError, zero_width)
        self.assertRaises(ValueError, zero_height)
        self.assertRaises(ValueError, wrong_orientation)

    def test_inconsistent_setup(self):
        x_greater_width = lambda: Rover(x = 2, width = 1)
        y_greater_height = lambda: Rover(y = 2, height = 1)
        x_equal_width = lambda: Rover(x = 5, width = 5)
        y_equal_height = lambda: Rover(y = 8, height = 8) 
        self.assertRaises(ValueError, x_greater_width)
        self.assertRaises(ValueError, y_greater_height)
        self.assertRaises(ValueError, x_equal_width)
        self.assertRaises(ValueError, y_equal_height)

    def test_forward_movement_north(self):
        rover = Rover(5, 5, 'N', 100, 100)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (5, 4))
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (5, 3))

    def test_forward_movement_east(self):
        rover = Rover(5, 5, 'E', 100, 100)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (6, 5))
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (7, 5))

    def test_forward_movement_south(self):
        rover = Rover(5, 5, 'S', 100, 100)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (5, 6))
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (5, 7))

    def test_forward_movement_west(self):
        rover = Rover(5, 5, 'W', 100, 100)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (4, 5))
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (3, 5))

    def test_backward_movement_north(self):
        rover = Rover(5, 5, 'N', 100, 100)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (5, 6))
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (5, 7))

    def test_backward_movement_east(self):
        rover = Rover(5, 5, 'E', 100, 100)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (4, 5))
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (3, 5))

    def test_backward_movement_south(self):
        rover = Rover(5, 5, 'S', 100, 100)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (5, 4))
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (5, 3))

    def test_backward_movement_west(self):
        rover = Rover(5, 5, 'W', 100, 100)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (6, 5))
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (7, 5))

    def test_wrap_movement_forward_north(self):
        rover = Rover(0, 0, 'N', 4, 4)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (0, 3))

    def test_wrap_movement_forward_east(self):
        rover = Rover(3, 0, 'E', 4, 4)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (0, 0))

    def test_wrap_movement_forward_south(self):
        rover = Rover(0, 3, 'S', 4, 4)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (0, 0))

    def test_wrap_movement_forward_west(self):
        rover = Rover(0, 0, 'W', 4, 4)
        rover = rover.forward()
        self.assertEqual(rover.get_position(), (3, 0))

    def test_wrap_movement_backward_north(self):
        rover = Rover(0, 3, 'N', 4, 4)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (0, 0))

    def test_wrap_movement_backward_east(self):
        rover = Rover(0, 0, 'E', 4, 4)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (3, 0))

    def test_wrap_movement_backward_south(self):
        rover = Rover(0, 0, 'S', 4, 4)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (0, 3))

    def test_wrap_movement_backward_west(self):
        rover = Rover(3, 0, 'W', 4, 4)
        rover = rover.backward()
        self.assertEqual(rover.get_position(), (0, 0))

    def test_rotation_right(self):
        rover = Rover(orientation = 'N')
        rover = rover.right()
        self.assertEqual(rover.get_orientation(), 'E')
        rover = rover.right()
        self.assertEqual(rover.get_orientation(), 'S')
        rover = rover.right()
        self.assertEqual(rover.get_orientation(), 'W')
        rover = rover.right()
        self.assertEqual(rover.get_orientation(), 'N')
        rover = rover.right().right().right().right()
        self.assertEqual(rover.get_orientation(), 'N')
        rover = rover.right().right().right().right().right().right()
        self.assertEqual(rover.get_orientation(), 'S')

    def test_rotation_left(self):
        rover = Rover(orientation = 'N')
        rover = rover.left()
        self.assertEqual(rover.get_orientation(), 'W')
        rover = rover.left()
        self.assertEqual(rover.get_orientation(), 'S')
        rover = rover.left()
        self.assertEqual(rover.get_orientation(), 'E')
        rover = rover.left()
        self.assertEqual(rover.get_orientation(), 'N')
        rover = rover.left().left().left().left()
        self.assertEqual(rover.get_orientation(), 'N')
        rover = rover.left().left().left().left().left().left()
        self.assertEqual(rover.get_orientation(), 'S')

if __name__ == '__main__':
    unittest.main()
