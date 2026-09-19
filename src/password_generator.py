import random
import string
import nltk
from abc import ABC, abstractmethod

# words = ["Alex", "Ali", "David", "Elena", "Ramirez"]


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

    
class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length
    def generate(self):
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

        print(self.characters)

    def generate(self):
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
            self,
            number_of_words: int = 4,
            separator: str = "-",
            capitalization: bool = False,
            vocab: list = None
            ):
        
        if vocab is None:
            self.vocab = ["Alex", "Ali", "David", "Elena", "Ramirez"]

        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalization = capitalization

    def generate(self):
        passwod_words = [random.choice(self.vocab) for _ in range(self.number_of_words)]
        if self.capitalization:
            passwod_words = [words.upper() for words in passwod_words]
        return self.separator.join(passwod_words)
    
if __name__ == "__main__":
    p_obj = RandomPasswordGenerator()
    print(p_obj.generate())
