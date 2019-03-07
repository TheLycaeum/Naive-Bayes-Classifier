import classifier
import pytest

def test_words_in_a_folder():
    path = '/home/fairoos/naive_byaes/pytest_data/training_data/sports data'
    assert classifier.words_in_a_folder(path) == ['clean', 'clean', 'forgettable', 'game', 'game', 'great', 'match']
    path1 = '/home/fairoos/naive_byaes/pytest_data/training_data/non_sports data'
    assert classifier.words_in_a_folder(path1) == ['close', 'election', 'election']

def test_possible_words():
    assert classifier.possible_words(Dir_of_data = '/home/fairoos/naive_byaes/pytest_data/training_data/') == 7

def test_stop_word():
    assert classifier.stop_word(['the', 'monkey', 'is', 'not', 'a', 'cat']) == ['monkey', 'cat']

def test_probability_dict():
    assert classifier.probability_dict(['game', 'match'], Dir_of_data = '/home/fairoos/naive_byaes/pytest_data/training_data/') == {'sports data': 9.111761218400412e-07, 'non_sports data': 3.038169126368391e-07}

def test_percent_calculator():
    assert classifier.percent_calculator({'sports data': 9.111761218400412e-07, 'non_sports data': 3.038169126368391e-07}) == {'sports data': 74.99434943117606, 'non_sports data': 25.005650568823928}

