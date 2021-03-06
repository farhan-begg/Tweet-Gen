from dictogram import Dictogram
from histogram import open_file
import random


class MarkovChain(dict):
    def __init__(self, word_list=None):

        super(MarkovChain, self).__init__()
        
        if word_list is not None:
            self.create_markov(word_list)

    
    def open_text(self, path = 'test.txt'):
        text = open_file(path)
    
        return text 
    

    def create_markov(self, word_list): 
        '''This method will create a 2nd order markovchain with word list'''
        num_words = len(word_list)  
        # loop through each key and increase index
        for index, key1 in enumerate(word_list):  #adds an index to a word 
            if num_words > index + 2:             #
                key2 = word_list[index + 1]
                word = word_list[index + 2]

                if (key1, key2) not in self:
                    self[(key1, key2)] = Dictogram([word])
                else:
                    self[(key1, key2)].add_count(word)


    def sentence(self, word_list, num_words):
        
        sentence = ""
        random_index = random.randint(0, len(word_list) - 1)
        key = (word_list[random_index], word_list[random_index + 1])

        while len(sentence) < num_words:  
            word = self[key].sample()
            sentence += " " + word
            key = (key[1], word)
        
        return sentence
                 

def word_generator():

    word_list = MarkovChain.open_text("test.txt")
    markov_chain = MarkovChain(word_list)

    return(markov_chain.sentence(word_list, 60))


if __name__ == "__main__":
    print(word_generator())