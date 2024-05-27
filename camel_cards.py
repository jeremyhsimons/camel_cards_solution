"""A program to play Camel Cards"""


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


def play_game():
    """
    A function to control the logic
    of Camel Cards.
    """
    inputs = split_input_string("inputs.txt")
    hands_with_types = find_hand_type(inputs)
    print(hands_with_types)


if __name__ == "__main__":
    play_game()
