import classifier
import pytest

def test_words_in_a_folder():
    path = '/home/fairoos/naive_byaes/pytest_data/training_data/sports lyrics'
    assert classifier.words_in_a_folder(path) == ['clean', 'clean', 'forgettable', 'game', 'game', 'great', 'match']
    path1 = '/home/fairoos/naive_byaes/pytest_data/training_data/non_sports lyrics'
    assert classifier.words_in_a_folder(path1) == ['close', 'election', 'election']

def test_possible_words:
    assert classifier.possible_words(['hello', 'hi', 'good']) == 3 

# def test_probability_word():
#     word = 'a'
#     assert classifier.probability_word(['a', 'b', 'd', 'a']) == 2/4
