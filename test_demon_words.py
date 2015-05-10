from demon_words import *

word_list = ["BIRD", "CALF", "RIVER", "STREAM", "KNEECAP",  "COOKBOOK",
             "LANGUAGE", "SNEAKER", "ALGORITHM", "INTEGRATION", "BRAIN"]

four_letter_words = ['LION', 'LIPS', 'LIRE', 'MIST', 'LOFT',
                     'MOST', 'LOCI', 'LOCK']

word_dict = {"_ I _ _": ["LION", "LIPS", "LIRE", "MIST"],
             "_ _ _ _": ["LOFT", "MOST", "LOCK"],
             "_ _ _ I": ["LOCI"]}

def test_list_of_words():
    assert list_of_words(word_list, 4) == ["BIRD", "CALF"]
    assert list_of_words(word_list, 8) == ["COOKBOOK", "LANGUAGE"]
    assert list_of_words(four_letter_words, 4) == ['LION', 'LIPS', 'LIRE', 'MIST',
                                                   'LOFT', 'MOST', 'LOCI', 'LOCK']

def test_cat_dict():
    assert cat_dict(four_letter_words, "I") == {"_ I _ _": ["LION", "LIPS", "LIRE", "MIST"],
                                                "_ _ _ _": ["LOFT", "MOST", "LOCK"],
                                                "_ _ _ I": ["LOCI"]}

def test_most_words_list():
    assert most_words_list(word_dict) == ["LION", "LIPS", "LIRE", "MIST"]
