class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, letter):
        """Gets text input from the terminal. Displays the guessed letter.

        Args: 
            self (TerminalService): An instance of TerminalService.
            letter (string): The letter to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(letter)
        
    def write_result(self, result):
        """Displays the result on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(result)