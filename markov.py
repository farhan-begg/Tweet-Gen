from dictogram import Dictogram
import random 
from histogram import open_file



def list_file():
    words_file = 'test.txt'
    text = open_file(words_file)
    words_list = []

    for word in text:
        words_list.append(word)

    return words_list


class Markov(dict):

    def __init__(self, words_list = None):
        super(Markov, self).__init__()

    # if words_list is not None:
    #     self.create_markov_chain(words_list)
    #     self['start'] = Dictogram(['the'])
    #     self['end'] = Dictogram([ ' . '])

    def create_markov_chain(self, words_list):

        for index, word in enumerate(words_list):

            if self.get(word) == None:
                self[word] = Dictogram()