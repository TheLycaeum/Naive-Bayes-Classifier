import classifier

def test_words_in_a_folder():
    path = '/home/fairoos/naive_byaes/sports'
    assert classifier.words_in_a_folder(path) == ['Very', 'clean', 'match', 'A', 'great', 'game', 'A', 'clean', 'but', 'forgettable', 'game']
