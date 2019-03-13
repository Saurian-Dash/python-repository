# Testing

# Doctests --- run "python -m doctest -v testing.py" to run doctests

def add(x, y):
    """
    >>> add(1, 2)
    3
    >>> add(1.5, 2.5)
    4.0
    >>> add('tree', 11)
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return x + y


# Unit Tests

import unittest
from utils.sleep import nap

class UtilTest(unittest.TestCase):
    
    def test_sleep(self):

        print(f'\nRunning unit tests...')
        self.assertEqual(
            nap(5),
            'I feel great after my 5 second nap!'
        )


if __name__ == '__main__':
    unittest.main()