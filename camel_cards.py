"""A program to play Camel Cards"""


CARD_STRENGTH = ["2", "3", "4", "5", "6", "7", "9", "T", "J", "Q", "K", "A"]


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


def insertion_sort(hands):
    """
    A function to sort hands smallest to largest.
    Insertion sort algorithm.
    """
    indexing_length = range(1, len(hands))
    for i in indexing_length:
        positive = i > 0
        # card_strengths = assess_higher_card(list_a[i-1][0], list_a[i][0])
        # print(list_a[i-1][0], list_a[i][0], card_strengths)
        # is_higher = card_strengths[1] > card_strengths[0]
        value_to_sort = hands[i][2]
        while hands[i-1][2] > value_to_sort and positive:
            hands[i], hands[i-1] = hands[i-1], hands[i]
            i = i - 1
            # card_strengths = assess_higher_card(list_a[i-1][0], list_a[i][0])
            # print("----", list_a[i-1][0], list_a[i][0], card_strengths)
            # print(TYPE_STRENGTH[list_a[i-1][2]] > value_to_sort)
            # is_higher = card_strengths[1] < card_strengths[0]

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
        while is_lower and positive and hands[i][2] == hands[i-1][2]:
            hands[i], hands[i-1] = hands[i-1], hands[i]
            i = i - 1
            card_strengths = assess_higher_card(hands[i-1][0], hands[i][0])
            is_lower = card_strengths[1] < card_strengths[0]

    return hands


def play_game():
    """
    A function to control the logic
    of Camel Cards.
    """
    inputs = split_input_string("inputs.txt")
    hands_with_types = find_hand_type(inputs)
    sorted_1 = insertion_sort(hands_with_types)
    # sorted_2 = insertion_sort(sorted_1)
    sorted_2 = sort_by_highest_card(sorted_1)
    print(sorted_2)


if __name__ == "__main__":
    play_game()
