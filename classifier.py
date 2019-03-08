import os
import re
import nltk
#nltk.download('wordnet')
#nltk.download('stopwords')

train_data = '/home/fairoos/naive_byaes/training_data/'
test_data = '/home/fairoos/naive_byaes/testing_data'

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
    #cont_list = lammatize(cont_list)
    cont_list = stop_word(cont_list)
    return cont_list

def possible_words(train_data):
    """to count all possible words in training data"""
    list_words = []
    for dir in os.listdir(train_data):
        path = ("{}{}".format(train_data, dir))
        list_words.extend(words_in_a_folder(path)) # combain lists
        list_words = list(dict.fromkeys(list_words)) # rm duplicates from List:
        list_words = stop_word(list_words)
    count = len(list_words)
    return count

def count_files(list_dir = os.listdir(train_data)):
    """coun files in a directory"""
    count = 0
    for dir in list_dir:
        count += len(os.listdir("{}{}".format(train_data, dir)))
    return count

def stop_word(input_words):
    from nltk.corpus import stopwords
    en_stops = set(stopwords.words('english'))
    all_words = input_words
    words = list()
    for word in all_words: 
        if word not in en_stops:
            words.append(word)    
    return words


# def lammatize(word_list):
#     from nltk.stem import WordNetLemmatizer
#     lemmatizer = WordNetLemmatizer()
#     lemmatized_output = [lemmatizer.lemmatize(w) for w in word_list]
#     return lemmatized_output

def probability_dict(cont_list, train_data):
    x = {}
    for dir in os.listdir(train_data):
        #print(dir)
        words =  words_in_a_folder('{}{}'.format(train_data,dir))
        b =[]
        for element in cont_list:
            count = 0
            for word in words:
                if element == word:
                    count += 1
            b.append(count)
        c = []
        for count in b:
            p_a_word = ((count + 1)/(len(words) + possible_words(train_data)))
            c.append(p_a_word)
        probability = 1
        for d in c:
            probability1 = probability * d
            total_files = count_files()
            file_me = len(os.listdir('{}{}'.format(train_data, dir)))
            prob_me = file_me / total_files
            total_porbability = probability1 * prob_me
            pro = format(float(total_porbability), '.20f')
            x.update({dir:total_porbability})
    return x

def percent_calculator(x):
    key_list = list()
    value_list = list()
    for i in x.keys():
        key_list.append(i)
        
    for j in x.values():
        value_list.append(j)
        
    sum_list = sum(value_list)
    perc_list = list()
    for i in value_list:
        try:
            percentage = (i/sum_list) * 100
            perc_list.append(percentage)
        except ZeroDivisionError:
            percentage = 0
    perce = dict()
    for key, perc in zip(key_list, perc_list):
        print("{} =  {} %.".format(key, perc))
        print()
        perce.update({key:perc})
    return perce
    
    
def probability(test_data, train_data):
    """ find the probability of testing data up on trained data"""
    prob_list = list()
    for filename in os.listdir(test_data):
        print(filename)
        print()
        file_path = os.path.join(test_data, filename)
        fil = open(file_path)
        content = fil.read()
        files_cont = re.sub(r'[^\w\s]','',content) #remove punctuation !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        cont_list = files_cont.split()
        cont_list.sort()
        cont_list = [x.lower() for x in cont_list] #to lower case all words
        #cont_list = lammatize(cont_list)
        cont_list = list( dict.fromkeys(cont_list)) #remove repeted words
        cont_list = stop_word(cont_list)
        x = probability_dict(cont_list, train_data)
        prob_list.append(percent_calculator(x))
        print("=== " * 34)
    return prob_list
#probability()
        
                


