import sys
import re


def open_file(words_file):
    '''Opens text file and arranges words into a readable list '''    

    with open (words_file, 'r') as f:
        words = f.read()
        scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    
    return scrubbed_words.split(" ")

def histogram_dict(words_file):
    '''Takes text argument and returns a histogram data structure in a dictionary form'''
    
    histogram = {}
    words = open_file(words_file) 
    
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1 
   
    return histogram

def histogram_list(words_file):
    '''Takes text argument and returns a histogram data structure in a list form'''
   
    words = open_file(words_file)
    histogram = []

    for word in words:
        for item in histogram:
            if item[0] == word:
                item[1] += 1
                break
        else:
            histogram.append([word, 1])

    return histogram

def histogram_tuples(words_file):
    '''Takes text argument and returns a histogram data structure in a tuples form '''
    
    words = histogram_list(words_file)
    histogram = []
    
    for item in words:
        histogram.append(tuple(item))

    return histogram


def unique_words(words_file):
    '''Takes a histogram argument and returns the total count of unique words in the histogram '''
   
    histogram = {}
    words = open_file(words_file)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else: 
            histogram[word] = 1
   
    print(len(histogram))

def frequency(search, words_file):
    '''Takes a word and histogram argument and returns the number of times t '''
   
    histogram = {}
    words = open_file(words_file)

    for word in words:
        if word in histogram:
            histogram[word] = histogram[word] + 1
        else: 
            histogram[word] = 1
    
    print(histogram.get(search, 0))


if __name__ == '__main__':

    words_file  = 'test.txt'

    histogram_dict(words_file)
    
    unique_words(words_file)
    frequency('fish', words_file)
