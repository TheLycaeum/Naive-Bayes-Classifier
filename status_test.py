import classifier
import os
test_data = '/home/fairoos/naive_byaes/testing_data'
train_data = '/home/fairoos/naive_byaes/training_data/'

def name_file(file_names = os.listdir(test_data)):
    file_name_list = []
    for filename in file_names:
        file_name_list.append(filename)
    return file_name_list
dictr =  classifier.probability(test_data, train_data)
def highest(dictr):
    #from classifier import probability
    global lenth
    lenth = len(dictr)
    keylist = list()
    for i in name_file():
        for j in dictr:
            value_list = list()
            for value in j.values():
                value_list.append(value)
            maxi = max(value_list)
            keylist.append(list(j.keys())[list(j.values()).index(maxi)])
        return keylist

def final_stat():
    file_names = name_file()
    sucess = 0
    feild = 0
    highest1 = highest(dictr)
    for file_name, high in zip(file_names, highest1):
        file_name_list = file_name.split()
        highest_list = high.split()
        file_name_list= [x.lower() for x in file_name_list]
        highest_list = [x.lower() for x in highest_list]
        if highest_list[0] == file_name_list[0]:
            sucess += 1
        else:
            feild += 1
    print(f"Your model predict {sucess} sucess and {feild} feil")
    print()
    sucess_perc = (sucess/lenth)* 100
    print(f"Your system is {sucess_perc} % accurate")
    stars = (int(sucess_perc/10)*'⭐ ')
    print()
    print(f"Your rating is {stars}")
    print()
    print("💖💖 ⮘⮘Thanks for use me⮚⮚ 💖💖")
    print()
    print("=== " * 34)
        
final_stat()
