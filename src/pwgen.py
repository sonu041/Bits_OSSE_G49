import random

UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SPECIAL = "!@#$%^&*()_+-={}[]\|<>,./?~"

class PwGenerator:

    def generate(
            self,
            length=15,
            include_numbers=False
        ):
        """
        Returns a random password
        
        Args:
            length (int): Length of the password
        """
        char_set = UPPER_CASE + LOWER_CASE
        
        if include_numbers is True:
            char_set = char_set + NUMBERS
            
        if include_special is True:
            char_set = char_set + SPECIAL
        
        chars = list(char_set)
        
        iterations = len(chars) * 5     # number of times to shuffle
        for _ in range(iterations):     # run a loop
            random.shuffle(chars)       # shuffle chars in place
            
        pw = chars[:length]

        pw_str = "".join(pw)            # join the characters into a string
        return pw_str                   # return password
