from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        if (self.get_text()=='*'):
            self._points = 1

        else: 
            self._point = -1

    return self._points    


        #self._message = ""
        
    #def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        #return self._message
    
    #def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        #self._message = message