import sys
from random import choice


# opens text file from location 
f = open("/usr/share/dict/words", "r")

word_list=f.readlines()

def random_word(amount):
    # Checks words in list and prints randomize words in range
    count = 0
    random = []
    f.close()

    while count < int(amount):
        random.append(choice(word_list).strip())
        count +=1
    return ' '.join(random)


if __name__ == "__main__":
    amount = sys.argv[1]
    output = random_word(amount)
    print(output)