import classifier

def test_words_in_a_folder():
    path = '/home/fairoos/naive_byaes/sports'
    assert classifier.words_in_a_folder(path) == ['A', 'A', 'Very', 'but', 'clean', 'clean', 'forgettable', 'game', 'game', 'great', 'match']
    path1 = '/home/fairoos/naive_byaes/non_sports'
    assert classifier.words_in_a_folder(path1) == ['It', 'The', 'The', 'a', 'barking', 'beautful', 'close', 'dogs', 'election', 'election', 'flower', 'over', 'was', 'was']
