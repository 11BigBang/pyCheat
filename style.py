"""A brief sentence describing this module.

This part may go a little in depth.

"""

# Standard library imports

# Third party imports

# Local imports

class Dog:
    """What this class is

    Some more details.

    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        """A one-line docstring to describe this function."""
        print('Woof!')

    def print_docstring(self):
        """Docstrings can be printed using the line below."""
        print(self.speak.__doc__)

dog = Dog('Lady')
dog.print_docstring()