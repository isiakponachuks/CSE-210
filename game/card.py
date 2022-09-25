import random

class Card:
    """
    An individual card with a different or random number from 1 to 13.

    The responsibility of Card is to keep track of the card drawn.
   
    Attributes:
        value (int): The number of the card drawn.
    """

    def __init__(self):
        """
        Constructs a new instance of Card with a value.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
    
    def drawn(self):
        """
        Generates a new random value.
        
        Args:
            self (Card): An instance of Card.
        """
        # Individual cards are represented as a number from 1 to 13.
        self.value = random.randint(1, 13)