import os
import re


def words_in_a_folder(path):
    """Total number of words in a folder"""
    files_cont = ''
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        fil = open(file_path)
        content = fil.read()
        files_cont += content
    files_cont = re.sub(r'[^\w\s]','',files_cont) #remove punctuation
    cont_list = files_cont.split()
    cont_list.sort()
    cont_list = [x.lower() for x in cont_list] #to lower case all words
    return cont_list

def possible_words():
    """to count all possible words in training data"""
    Dir_of_data = '/home/fairoos/naive_byaes/training_data/'
    list_words = []
    for dir in os.listdir(Dir_of_data):
        path = (f"/home/fairoos/naive_byaes/training_data/{dir}")
        list_words.extend(words_in_a_folder(path)) # combain lists
        list_words = list(dict.fromkeys(list_words)) # rm duplicates from List:
    count = len(list_words)
    return count


    
