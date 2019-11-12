import random
import sys

def rearrange(words_list):
    # rearrange given word
    for i, word in enumerate(words_list):
        random_index = random.randint(0, len(words_list) - 1)
        words_list[i] = words_list[random_index]
        words_list[random_index] = word

    return words_list
    # return word_list 

if __name__ == '__main__':
    word_list = sys.argv[1:]
    rearrange(word_list)
    print(' '.join(word_list))