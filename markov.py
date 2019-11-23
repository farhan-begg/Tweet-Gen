# from dictogram import Dictogram
# import random 
# from histogram import open_file

# def open_file(words_file):
#     '''Opens text file and arranges words into a readable list '''    

#     with open (words_file, 'r') as f:
#         words = f.read()
#         scrubbed_words = re.sub(r'[^a-zA-Z\s]', '', words)
    
#     return scrubbed_words.split(" ")



# def generate_sentence(chain, count=15):

#     word1 = random.choice(list(chain.keys()))
    
#     for i in range(count-1):
#         word2 = random.choice(chain[word1])
#         word1 = word2
#         sentence += ' ' + word2

#     return(sentence )

# words_file = ('test.txt')
# generate_sentence(ali_dict)

