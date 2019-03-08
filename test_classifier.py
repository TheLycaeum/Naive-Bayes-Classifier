import classifier
#import pytest
import status_test
import os

train_data = '/home/fairoos/naive_byaes/pytest_data/training_data/'
test_data = '/home/fairoos/naive_byaes/pytest_data/testing_data'

def test_words_in_a_folder():
    path = '/home/fairoos/naive_byaes/pytest_data/training_data/sports data'
    assert classifier.words_in_a_folder(path) == ['clean', 'clean', 'forgettable', 'game', 'game', 'great', 'match']
    path1 = '/home/fairoos/naive_byaes/pytest_data/training_data/non_sports data'
    assert classifier.words_in_a_folder(path1) == ['close', 'election', 'election']

def test_possible_words():
    assert classifier.possible_words(train_data) == 7

def test_stop_word():
    assert classifier.stop_word(['the', 'monkey', 'is', 'not', 'a', 'cat']) == ['monkey', 'cat']

def test_probability_dict():
    assert classifier.probability_dict(['game', 'match'], train_data) == {'sports data': 0.0008640552995391705, 'non_sports data': 0.0004032258064516129}

def test_percent_calculator():
    assert classifier.percent_calculator({'sports data': 9.111761218400412e-07, 'non_sports data': 3.038169126368391e-07}) == {'sports data': 74.99434943117606, 'non_sports data': 25.005650568823928}

def test_probability():
    assert classifier.probability(test_data, train_data) == [{'non_sports data': 48.275862068965516, 'sports data': 51.72413793103448}, {'non_sports data': 31.818181818181824, 'sports data': 68.18181818181819}]

def test_status_test():
    assert status_test.name_file(file_names = os.listdir(test_data)) == ['non_sports data', 'sports data']

def test_highest():
    assert status_test.highest([{'non_sports data': 48.275862068965516, 'sports data': 51.72413793103448}, {'non_sports data': 31.818181818181824, 'sports data': 68.18181818181819}]) == ['sports data', 'sports data']
