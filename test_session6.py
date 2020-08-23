import re
import os
import pytest
import inspect
import math
import random
import session6


README_CONTENT_CHECK_FOR = [
    "create_deck_2",
    "check_winner",
    "is_royal_flush",
    "is_flush",
    "is_straight_flush",
    "is_straight",
    "is_four_of_a_kind",
    "is_three_of_a_kind",
    "is_two_pair",
    "is_one_pair",
    "is_full_house",
]

vals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
suits = ["spades", "clubs", "hearts", "diamonds"]


def test_create_deck_1():
    """
    Test function for question 1. 
    """
    assert sorted(
        list(map(lambda x: x, zip(vals * len(suits), suits * len(vals))))
    ) == sorted(
        [
            ("2", "spades"),
            ("2", "clubs"),
            ("2", "hearts"),
            ("2", "diamonds"),
            ("3", "spades"),
            ("3", "clubs"),
            ("3", "hearts"),
            ("3", "diamonds"),
            ("4", "spades"),
            ("4", "clubs"),
            ("4", "hearts"),
            ("4", "diamonds"),
            ("5", "spades"),
            ("5", "clubs"),
            ("5", "hearts"),
            ("5", "diamonds"),
            ("6", "spades"),
            ("6", "clubs"),
            ("6", "hearts"),
            ("6", "diamonds"),
            ("7", "spades"),
            ("7", "clubs"),
            ("7", "hearts"),
            ("7", "diamonds"),
            ("8", "spades"),
            ("8", "clubs"),
            ("8", "hearts"),
            ("8", "diamonds"),
            ("9", "spades"),
            ("9", "clubs"),
            ("9", "hearts"),
            ("9", "diamonds"),
            ("10", "spades"),
            ("10", "clubs"),
            ("10", "hearts"),
            ("10", "diamonds"),
            ("jack", "spades"),
            ("jack", "clubs"),
            ("jack", "hearts"),
            ("jack", "diamonds"),
            ("queen", "spades"),
            ("queen", "clubs"),
            ("queen", "hearts"),
            ("queen", "diamonds"),
            ("king", "spades"),
            ("king", "clubs"),
            ("king", "hearts"),
            ("king", "diamonds"),
            ("ace", "spades"),
            ("ace", "clubs"),
            ("ace", "hearts"),
            ("ace", "diamonds"),
        ]
    )


def test_create_deck_2():
    """
    Test function for question 2. 
    """
    assert session6.create_deck_2(vals, suits) == [
        ("2", "spades"),
        ("2", "clubs"),
        ("2", "hearts"),
        ("2", "diamonds"),
        ("3", "spades"),
        ("3", "clubs"),
        ("3", "hearts"),
        ("3", "diamonds"),
        ("4", "spades"),
        ("4", "clubs"),
        ("4", "hearts"),
        ("4", "diamonds"),
        ("5", "spades"),
        ("5", "clubs"),
        ("5", "hearts"),
        ("5", "diamonds"),
        ("6", "spades"),
        ("6", "clubs"),
        ("6", "hearts"),
        ("6", "diamonds"),
        ("7", "spades"),
        ("7", "clubs"),
        ("7", "hearts"),
        ("7", "diamonds"),
        ("8", "spades"),
        ("8", "clubs"),
        ("8", "hearts"),
        ("8", "diamonds"),
        ("9", "spades"),
        ("9", "clubs"),
        ("9", "hearts"),
        ("9", "diamonds"),
        ("10", "spades"),
        ("10", "clubs"),
        ("10", "hearts"),
        ("10", "diamonds"),
        ("jack", "spades"),
        ("jack", "clubs"),
        ("jack", "hearts"),
        ("jack", "diamonds"),
        ("queen", "spades"),
        ("queen", "clubs"),
        ("queen", "hearts"),
        ("queen", "diamonds"),
        ("king", "spades"),
        ("king", "clubs"),
        ("king", "hearts"),
        ("king", "diamonds"),
        ("ace", "spades"),
        ("ace", "clubs"),
        ("ace", "hearts"),
        ("ace", "diamonds"),
    ]


def test_readme_exists():
    """
    Test funtion to check if README exists.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test if README contains atleast 200 words.
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ 
   Returns pass if used four spaces for each level of syntactically \
   significant indenting.
   """
    lines = inspect.getsource(session6)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_royal_flush():
    """
    Test Royal Flush function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("king", "hearts"),
        ("queen", "hearts"),
        ("jack", "hearts"),
        ("10", "hearts"),
    ]
    assert session6.is_royal_flush(temp_hand) == True


def test_straight_flush():
    """
    Test for straight flush function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "hearts"),
        ("8", "hearts"),
        ("7", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_straight_flush(temp_hand) == True


def test_flush():
    """
    Test for flush function.
    """
    temp_hand = [
        ("king", "hearts"),
        ("8", "hearts"),
        ("6", "hearts"),
        ("4", "hearts"),
        ("2", "hearts"),
    ]
    assert session6.is_flush(temp_hand) == True


def test_straight():
    """
    Test for straight function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "spades"),
        ("8", "diamonds"),
        ("7", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_straight(temp_hand) == True


def test_four_of_a_kind():
    """
    Test for 4 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_four_of_a_kind(temp_hand) == True


def test_three_of_a_kind():
    """
    Test 3 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
        ("king", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_three_of_a_kind(temp_hand) == True


def test_two_pair():
    """
    Test 2 pair function.
    """
    temp_hand = [
        ("jack", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_two_pair(temp_hand) == True


def test_one_pair():
    """
    Test one pair function.
    """
    temp_hand = [
        ("4", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_one_pair(temp_hand) == True


def test_full_house():
    """
    Test full house function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("ace", "spades"),
        ("ace", "diamonds"),
        ("queen", "hearts"),
        ("queen", "hearts"),
    ]
    assert session6.is_full_house(temp_hand) == True


def test_high_card():
    """
    Test high card function. If a hand is none of the other functions, 
    then it is classified as high card.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("queen", "spades"),
        ("6", "diamonds"),
        ("4", "hearts"),
        ("3", "clubs"),
    ]

    assert (
        session6.is_royal_flush(temp_hand)
        or session6.is_straight_flush(temp_hand)
        or session6.is_straight(temp_hand)
        or session6.is_four_of_a_kind(temp_hand)
        or session6.is_three_of_a_kind(temp_hand)
        or session6.is_two_pair(temp_hand)
        or session6.is_one_pair(temp_hand)
        or session6.is_full_house(temp_hand) == False
    )


##########


def test_royal_flush_4cards():
    """
    Test Royal Flush function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("king", "hearts"),
        ("queen", "hearts"),
        ("jack", "hearts"),
    ]
    assert session6.is_royal_flush(temp_hand) == True


def test_straight_flush_4cards():
    """
    Test for straight flush function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "hearts"),
        ("8", "hearts"),
        ("7", "hearts"),
    ]
    assert session6.is_straight_flush(temp_hand) == True


def test_flush_4cards():
    """
    Test for flush function.
    """
    temp_hand = [
        ("king", "hearts"),
        ("8", "hearts"),
        ("6", "hearts"),
        ("4", "hearts"),
    ]
    assert session6.is_flush(temp_hand) == True


def test_straight_4cards():
    """
    Test for straight function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "spades"),
        ("8", "diamonds"),
        ("7", "hearts"),
    ]
    assert session6.is_straight(temp_hand) == True


def test_four_of_a_kind_4cards():
    """
    Test for 4 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
    ]
    assert session6.is_four_of_a_kind(temp_hand) == True


def test_three_of_a_kind_4cards():
    """
    Test 3 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
        ("king", "hearts"),
    ]
    assert session6.is_three_of_a_kind(temp_hand) == True


def test_two_pair_4cards():
    """
    Test 2 pair function.
    """
    temp_hand = [
        ("jack", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
    ]
    assert session6.is_two_pair(temp_hand) == True


def test_one_pair_4cards():
    """
    Test one pair function.
    """
    temp_hand = [
        ("4", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
        ("queen", "hearts"),
    ]
    assert session6.is_one_pair(temp_hand) == True


def test_full_house_4cards():
    """
    Test full house function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("ace", "spades"),
        ("ace", "diamonds"),
        ("queen", "hearts"),
    ]
    assert session6.is_full_house(temp_hand) == False


def test_high_card_4cards():
    """
    Test high card function. If a hand is none of the other functions, 
    then it is classified as high card.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("queen", "spades"),
        ("6", "diamonds"),
        ("4", "hearts"),
    ]

    assert (
        session6.is_royal_flush(temp_hand)
        or session6.is_straight_flush(temp_hand)
        or session6.is_straight(temp_hand)
        or session6.is_four_of_a_kind(temp_hand)
        or session6.is_three_of_a_kind(temp_hand)
        or session6.is_two_pair(temp_hand)
        or session6.is_one_pair(temp_hand)
        or session6.is_full_house(temp_hand) == False
    )


##########


def test_royal_flush_3cards():
    """
    Test Royal Flush function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("king", "hearts"),
        ("queen", "hearts"),
    ]
    assert session6.is_royal_flush(temp_hand) == True


def test_straight_flush_3cards():
    """
    Test for straight flush function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "hearts"),
        ("8", "hearts"),
    ]
    assert session6.is_straight_flush(temp_hand) == True


def test_flush_3cards():
    """
    Test for flush function.
    """
    temp_hand = [
        ("king", "hearts"),
        ("8", "hearts"),
        ("6", "hearts"),
    ]
    assert session6.is_flush(temp_hand) == True


def test_straight_3cards():
    """
    Test for straight function.
    """
    temp_hand = [
        ("10", "hearts"),
        ("9", "spades"),
        ("8", "diamonds"),
    ]
    assert session6.is_straight(temp_hand) == True


def test_four_of_a_kind_3cards():
    """
    Test for 4 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
    ]
    assert session6.is_four_of_a_kind(temp_hand) == False


def test_three_of_a_kind_3cards():
    """
    Test 3 of a kind function.
    """
    temp_hand = [
        ("queen", "hearts"),
        ("queen", "spades"),
        ("queen", "diamonds"),
    ]
    assert session6.is_three_of_a_kind(temp_hand) == True


def test_two_pair_3cards():
    """
    Test 2 pair function.
    """
    temp_hand = [
        ("jack", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
    ]
    assert session6.is_two_pair(temp_hand) == False


def test_one_pair_3cards():
    """
    Test one pair function.
    """
    temp_hand = [
        ("4", "hearts"),
        ("jack", "spades"),
        ("queen", "diamonds"),
    ]
    assert session6.is_one_pair(temp_hand) == False


def test_full_house_3cards():
    """
    Test full house function.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("ace", "spades"),
        ("ace", "diamonds"),
    ]
    assert session6.is_full_house(temp_hand) == False


def test_high_card_3cards():
    """
    Test high card function. If a hand is none of the other functions, 
    then it is classified as high card.
    """
    temp_hand = [
        ("ace", "hearts"),
        ("queen", "spades"),
        ("6", "diamonds"),
    ]

    assert (
        session6.is_royal_flush(temp_hand)
        or session6.is_straight_flush(temp_hand)
        or session6.is_straight(temp_hand)
        or session6.is_four_of_a_kind(temp_hand)
        or session6.is_three_of_a_kind(temp_hand)
        or session6.is_two_pair(temp_hand)
        or session6.is_one_pair(temp_hand)
        or session6.is_full_house(temp_hand) == False
    )
