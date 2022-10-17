import string
import random
from english_words import english_words_lower_set

class PasswordGenerator:
    __password_length = 12
    __password_type = "string"
    __divider = ""

    def __init__(self, options: dict[str, str]) -> None:
        for o in options:
            if o == "-p" or o == "--phrase":
                self.__password_type = "phrase"
            elif o == "-l" or o == "--length":
                self.__password_length = int(options[o])
            elif o == "-d" or o == "--divide":
                self.__divider = options[o]

    def generate(self) -> str:
        password = self.__build_phrase_password() if self.__password_type == "phrase" else self.__build_string_password()
        return password

    def __build_string_password(self) -> str:
        chars = self.__get_password_characters()
        p = ""

        for _ in range(self.__password_length):
            p += random.choice(chars)

        return p

    def __build_phrase_password(self) -> str:
        p = ""

        for i in range(self.__password_length):
            word = random.choice(tuple(english_words_lower_set))
            word = word.capitalize()
            p += word

            if (i + 1 < self.__password_length and self.__divider != ""):
                p += self.__divider

        return p

    def __get_password_characters(self):
        letters = list(string.ascii_letters)
        numbers = list(string.digits)
        special = list("!@#$%^&*-")
        return letters + numbers + special
