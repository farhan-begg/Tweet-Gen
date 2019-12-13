import random
from histogram import histogram_dict


def random_word(histogram, count):
    '''returns a random word '''
    total = 0
    index = random.randint(1, count)
    
    for key, value in histogram.items():
        total += value
        
        if index <= total:  
            return key

def main_sample(words_file):
   
    words = histogram_dict(words_file)
    count = sum(words.values())
    word = random_word(words, count)
    
    return (word)

if __name__ == '__main__':
    words_file = 'test.txt'
    histogram = histogram_dict(words_file)
    print(random_word(histogram, 100))

