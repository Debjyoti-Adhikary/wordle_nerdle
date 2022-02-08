import nltk
import random
from nltk.corpus import words

class Wordle():
    def __init__(self,word_length=5,max_attempts=6):
        self.word_length = word_length
        self.max_attempts = max_attempts
        # self.get_word_list(word_length)
        self.generate_result()

    # def get_word_list(self,word_len=5):
    #     all_words = words.words()
    #     ### will have to use trie
    #     self.word_list = [word for word in all_words if len(word) == word_len]
    #     self.word_count = len(self.word_list)

    def generate_result(self):
        self.gold_word = random.choice([word for word in words.words() if len(word) == self.word_length])

    def check_attempts(self,input_word,attempts=0,):
        if attempts < self.max_attempts:
            if input_word == self.final_result:
                #return 1 for green
                return [1]*self.word_length
            else:
                #need to change the input color based on the final result
                return 0

    # def get_user_input(self,input_word):
    #     attempt = 0
    #     while attempt < self.max_attempts:




wordle = Wordle()
print(wordle.generate_result())

def check(input_word,gold_word):
    print(input_word,gold_word)
    input_dict = {}
    for idx,character in enumerate(input_word):
        if character not in input_dict:
            input_dict[character] = []
        input_dict[character].append(idx)

    gold_word_dict = {}
    for idx,character in enumerate(gold_word):
        if character not in gold_word_dict:
            gold_word_dict[character] = []
        gold_word_dict[character].append(idx)

    print(input_dict,gold_word_dict)

    response = [-2]*len(input_word)
    for letter in input_dict:
        matchedCount = []
        if letter not in gold_word_dict:
            for idx in input_dict[letter]:
                response[idx] = -1
            continue
        for idx in input_dict[letter]:
            if idx in gold_word_dict[letter]:
                matchedCount.append(idx)

        if len(matchedCount) == len(input_dict[letter]):
            for idx in input_dict[letter]:
                response[idx] = 1
        else:
            currCount = 0
            for idx in input_dict[letter]:
                if idx in matchedCount:
                    response[idx] = 1
                elif len(gold_word_dict[letter]) - len(matchedCount) >currCount:
                    response[idx] = 0
                    currCount += 1
                else:
                    response[idx] = -1
                    currCount += 1
    return response

input
print(check("smiles","smiles"))


'''
# ans : OKUAC
# input: CUOOO
# 
# 
# [0, 0, 0, 0, -1]
# 
# 
# {O: [3], K: [1], U: [2], A: [3], C: [4]}
# 
# {O: [2,3,4], K: [2], U: [1], C: [0]}
response = [-2, -2, -2, -2, -2]
for letter in input_dict:
    matchedCount = []
    if letter is not in gold_word_dict:
            for idx in input_dict[letter]:
                response[idx] = -1
    for idx in input_dict[letter]:
        if idx in gold_word_dict[letter]:
            matchedCount.append(idx)

    if len(matchedCount) == len(input_dict[letter]):
        for idx in input_dict[letter]:
            response[idx] = 1
    else:
        currCount = 0
        for idx in input_dict[letter]:
            if idx in matchedCount:
                response[idx] = 1
            elif len(gold_word_dict[letter]) - 
                        len(matchedCount) > 
                        currCount:
                response[idx] = 0
                currCount += 1
            else:
                response[idx] = -1
                currCount += 1

[_, _, 0, 1, 0]


len(gold_word_dict[letter] == len(matchedCount):
                response[idx] = -1
            elif len(gold_word_dict[letter] > len(matchedCount):
                if len(gold_word_dict[letter] - len(matchedCount) > currCount:
                    response[idx] = 0
                else:
                    response[idx] = -1
            elif len(gold_word_dict[letter] > len(matchedCount)

'''
##########
'''
gold_word: OKUAC
input: CUOOO

response = [-2, -2, 1, 1, 0, 0, -1]


gold_word_dict: {O: [1,2,3,6], K: [1], U: [2], A: [3], C: [4]}

input_dict: {O: [2,3,4,5,7], K: [2], U: [1], C: [0]}


matchedCount = [2,3]

currCount = 2

idx = 7


len(gold_word_dict[letter]) = kitne chahiye

len(matchedCount) = kitne exactly place hue hai

currCount = kitne matched hai but location galat hai

len(gold_word_dict[letter]) > len(input_dict[letter])
len(gold_word_dict[letter]) == len(input_dict[letter])
len(gold_word_dict[letter]) < len(input_dict[letter])


'''