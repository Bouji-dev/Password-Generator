import random
import string
import nltk
from abc import ABC , abstractmethod


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length
        
    def generate(self) -> str:
        return "".join([random.choice(string.digits) for _ in range(self.length)])
    



class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False ):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation    

    def generate(self):
                return "".join([random.choice(self.characters) for _ in range(self.length)])    
    
class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
            self,
            num_of_words: int = 4,
            separator: str = '-',
            capitalize: bool = False ,
            vocabulary: list = None
        ):

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.vocabulary = vocabulary
        self.num_of_words = num_of_words
        self.separators = separator
        self.capitalize = capitalize

    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)] 
        if self.capitalize:
            password_words = [word.upper() if random.choice([True,False]) else word.lower() for word in password_words]
        return self.separators.join(password_words) 
