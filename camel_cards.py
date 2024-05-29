"""
A program to play Camel Cards

The program needs to do the following to solve the problem:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PART 1:

1. Read a 'hand' of cards and assign it a score based on
what type it is.
(check_hand_type)

2. Assess which of two hands has the first high card
(assess_higher_card)

3. Sort the list of hands by their type
as well as by which hands have higher scoring cards sooner.
(sort_by_type, sort_by_highest_card)

4. Assign a rank to each hand once sorted, multiply by the bid,
and return the sum of all the bids.
(rank_hands, find_total_winnings)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PART 2:

The program needs to be able to recognise "J" as wild and
assign hands the correct type accordingly.

The program needs to recognise "J" as the lowest card.

It needs to keep treating all other hands without "J"
as they were treated in part 1.

"""


CARD_STRENGTH = [
    "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"
]
NEW_RULE_CARD_STRENGTH = [
    "J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"
]


def split_input_string(file_path):
    """
    A function to read the input data
    and load into appropriate data structure.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    inputs = []
    for line in lines:
        line = line.split()
        line[1] = int(line[1])
        inputs.append(line)

    return inputs


def check_hand_type(input_hand):
    """
    A function that returns the type of hand based on the cards.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Ideas for updating this part of the solution to handle
    the wildcard rule:

    1. After the hashmap is created, check whether "J" exists

    2. If so, iterate through keys/values to find the most common
    card in a copy of the hashmap minus jacks. 
    if all values in hashmap are 1, return score
    for 1 pair (it's not possible for a hand with a jack to be less
    than 1 pair).

    3. find the number of jacks in the hand.

    4. add a new record to the hashmap for the sum of the number
    of jacks and the other most common card value.

    5. remove jack and common card value from the hashmap

    6. execute the rest of the function as normal.

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    hash_map = {}
    for card in input_hand:
        if card in hash_map:
            hash_map[card] += 1
        else:
            hash_map[card] = 1

    if len(hash_map) == 1:
        return 7
    if len(hash_map) == 4:
        return 2
    if len(hash_map) == 5:
        return 1

    quantities = []
    for key, value in hash_map.items():
        quantities.append(value)

    if len(hash_map) == 2 and 1 in quantities:
        return 6

    if len(hash_map) == 2 and 2 in quantities:
        return 5

    if len(hash_map) == 3 and 3 in quantities:
        return 4

    if len(hash_map) == 3 and 2 in quantities:
        return 3


def find_hand_type(hands):
    """
    A function that assigns a score to each hand
    based on the hand type
    """
    for hand in hands:
        hand_type = check_hand_type(hand[0])
        hand.append(hand_type)
    return hands


def sort_by_type(hands):
    """
    A function to sort hands smallest to largest.
    Insertion sort algorithm.
    """
    indexing_length = range(1, len(hands))
    for i in indexing_length:
        positive = i > 0
        value_to_sort = hands[i][2]
        while hands[i-1][2] > value_to_sort and positive:
            hands[i], hands[i-1] = hands[i-1], hands[i]
            i = i - 1

    return hands


def assess_higher_card(list_1, list_2):
    """
    loops through all the cards and checks against mapping
    to see which hand is the strongest. 
    """
    for i, value in enumerate(list_1):
        if value == list_2[i]:
            continue
        list_1_strength = 0
        list_2_strength = 0
        for j, card in enumerate(CARD_STRENGTH):
            if card == list_1[i]:
                list_1_strength = j
            if card == list_2[i]:
                list_2_strength = j
        return [list_1_strength, list_2_strength]
    return [0, 0]


def sort_by_highest_card(hands):
    """
    A sorting algorithm to order hands
    according to which has the first highest card.
    """
    indexing_length = range(1, len(hands))
    for i in indexing_length:
        positive = i > 0
        card_strengths = assess_higher_card(hands[i-1][0], hands[i][0])
        is_lower = card_strengths[1] < card_strengths[0]
        # lower score, positive index, same hand type.
        while is_lower and positive and hands[i][2] == hands[i-1][2]:
            hands[i], hands[i-1] = hands[i-1], hands[i]
            i = i - 1
            card_strengths = assess_higher_card(hands[i-1][0], hands[i][0])
            is_lower = card_strengths[1] < card_strengths[0]

    return hands


def rank_hands(hands):
    """
    A function to give all the hands a rank
    which can then be used to multiply bids.
    """
    for i in range(len(hands)):
        hands[i].append(i+1)
    return hands


def find_total_winnings(hands):
    """ 
    A function that mutliplies all the winnings by
    each hand's rank and sums them.
    """
    total = 0
    for hand in hands:
        total += hand[1] * hand[3]
    return total


def play_game():
    """
    A function to control the logic
    of Camel Cards.
    """
    inputs = split_input_string("inputs.txt")
    hands_with_types = find_hand_type(inputs)
    sorted_1 = sort_by_type(hands_with_types)
    sorted_2 = sort_by_highest_card(sorted_1)
    ranked = rank_hands(sorted_2)
    total_winnings = find_total_winnings(ranked)
    print(sorted_2)
    return total_winnings


if __name__ == "__main__":
    winnings = play_game()
    print(winnings)
    # correct answer for part 1:
    # 253205868
