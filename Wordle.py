import nltk
import random
from nltk.corpus import words
# word_list = words.words()
# five_letter_words = [word for word in word_list if len(word)==5]
# five_count = len(five_letter_words)

class Wordle():
    def __init__(self,word_length=5,attempts=6):
        self.word_length = word_length
        self.attempts = attempts
        self.word_list = get_word_list(word_length)

    def get_word_list(word_len=5):
        all_words = words.words()
        word_list = [word for word in all_words if len(word) == word_len]
        word_count = len(word_list)
        return word_list, word_count

    def get_word():
        return random.choice(self.word_list)


# five_letter_words,five_count = get_word_list(word_len=5)
# result = get_word(five_letter_words)
# print(result)

wordle = Wordle()
print(wordle.get_word())