import random

class Parachute:
    """Contains random word
        Attributes:
            secret_words (List[]): List of secret words.
        """

    def __init__(self):
        """Constructs a new instance of secret words.

        Args:
            self (SecretWords): An instance of secret words.
        """
        self._secret_words = ["joyful","sadness","bark","house"]
        self._guess = ""

    def _choose_random_word(self):
        """Chooses a random word from the list.
            
            Args:
                self (SecretWords): An instance of secret words.
            """ 
        self._secret_word = random.choice(self._secret_words)
        
        return self._secret_word
        
    def _display_parachute(self, secret_word): 
        self._length = len(secret_word)
        self._display_letters = "_ " * self._length
        print(self._display_letters)
        
        print("  ___\n"
              "/ ___ \ \n"
              "\     / \n"
              " \   / \n"
              "   0\n"
              "  /|\ \n"
              "  / \ \n"
              "^^^^^^^"
        )
    def _check_guess(self, guess, secret_word):
        """Gets the current guess
        
        Returns:
            result: if the letter is correct or incorrect
        """
        if guess in secret_word:
            index = secret_word.find(guess)
            self._display_letters[index] == guess
    
        print(self._display_letters)
