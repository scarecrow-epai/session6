import itertools


vals = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
suits = ["spades", "clubs", "hearts", "diamonds"]


royal_flush = ["jack", "queen", "king", "ace"]

create_deck_1 = list(map(lambda x: x, zip(vals * len(suits), suits * len(vals))))


def create_deck_2(lst1: "list", lst2: "list"):
    """
    Create a deck of 52 cards for answer 2. Use Nested loops
    to to create all combos.
    Input: Two lists
    Output: Combined list
    """
    deck_list = []
    for i in lst1:
        for j in lst2:
            deck_list.append((i, j))

    return deck_list


def is_royal_flush(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify royal flush.
    Return false if all suits are not the same. Else, check for 
    royal flush combo.
    """
    hand_suit = cards[0][1]

    if not all(c[1] == hand_suit for c in cards):
        return False

    royal_flush = ["ace", "king", "queen", "jack", "10"]

    return all(x[0] == y for x, y in zip(cards, royal_flush))


def is_flush(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify flush.
    Check if all suits are same. Else return False.
    """
    hand_suit = cards[0][1]

    if not all(c[1] == hand_suit for c in cards):
        return False
    return True


def is_straight_flush(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify straight flush.
    Check if all suits are same and all vals are in a sequence.
    """
    hand_suit = cards[0][1]

    if not all(c[1] == hand_suit for c in cards):
        return False

    card_idx = [vals.index(c[0]) for c in cards]

    return card_idx == list(range(max(card_idx), min(card_idx) - 1, -1))


def is_straight(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify straight.
    Check if values are in sequence.
    """
    card_idx = [vals.index(c[0]) for c in cards]
    return card_idx == list(range(max(card_idx), min(card_idx) - 1, -1))


def is_four_of_a_kind(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify four of a kind.
    Check if 4 cards of same suit exists.
    """
    for v in vals:
        temp_val_count = 0
        for c in cards:
            if c[0] == v:
                temp_val_count += 1
        if temp_val_count >= 4:
            return True

    return False


def is_three_of_a_kind(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify three of a kind.
    Check if three cards of same suit exist.
    """
    for v in vals:
        temp_val_count = 0
        for c in cards:
            if c[0] == v:
                temp_val_count += 1
        if temp_val_count >= 3:
            return True

    return False


def is_two_pair(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify two pair.
    Create a temp counter dict and then count the number of 
    two pair occurence.
    """
    temp_count_dict = {k[0]: 0 for k in cards}
    temp_pair_count = 0

    for c in cards:
        temp_count_dict[c[0]] += 1

    for v in temp_count_dict.values():
        if v == 2:
            temp_pair_count += 1

    return temp_pair_count == 2


def is_one_pair(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify one pair.
    Create a temp counter dict to count the occurence
    of single pair of cards with same suit.
    """
    temp_count_dict = {k[0]: 0 for k in cards}
    temp_pair_count = 0

    for c in cards:
        temp_count_dict[c[0]] += 1

    for v in temp_count_dict.values():
        if v == 2:
            temp_pair_count += 1

    return temp_pair_count == 1


def is_full_house(cards: "list of tuples") -> "Bool":
    """
    Helper function to identify full house.
    Count full house by creating a temp counter dict.
    """
    temp_count_dict = {k[0]: 0 for k in cards}
    temp_three_count = 0
    temp_two_count = 0

    for c in cards:
        temp_count_dict[c[0]] += 1

    for v in temp_count_dict.values():
        if v == 3:
            temp_three_count += 1
        elif v == 2:
            temp_two_count += 1

    return temp_three_count and temp_two_count


def check_winner(
    cards1: "list of tuples", cards2: "list of tuples"
) -> "integers1, 0, -1":
    """
    Check winner between 2 hands of cards by testing various combos.
        Input: Twop decks of cards (of lengths 3/4/5)
        Output:
            0: if player one wins.
            1: if player two wins.
            -1: No winner. Tie.
    """
    if len(cards1) != len(cards2):
        raise ValueError("Card length should be same.")

    if len(cards1) < 3 or len(cards1) > 5:
        raise ValueError("Number of cards can be atmost 5.")

    cards1 = sorted(cards1, key=lambda x: vals.index(x[0]), reverse=True)
    cards2 = sorted(cards2, key=lambda x: vals.index(x[0]), reverse=True)

    check_list = [
        is_royal_flush,
        is_straight_flush,
        is_four_of_a_kind,
        is_full_house,
        is_flush,
        is_straight,
        is_three_of_a_kind,
        is_two_pair,
        is_one_pair,
    ]
    cards1_result = []
    cards2_result = []

    for check_func in check_list:
        cards1_result.append(int(check_func(cards1)))
        cards2_result.append(int(check_func(cards2)))

    for i, j in zip(cards1_result, cards2_result):
        if i > j:
            return 0
        if i < j:
            return 1
        else:
            pass

        return -1


cards1 = [
    ("ace", "hearts"),
    ("king", "hearts"),
    ("queen", "hearts"),
    ("jack", "hearts"),
    ("10", "hearts"),
]


cards2 = [
    ("2", "hearts"),
    ("king", "hearts"),
    ("3", "spades"),
    ("jack", "clubs"),
    ("10", "hearts"),
]


print(check_winner(cards1, cards2))
