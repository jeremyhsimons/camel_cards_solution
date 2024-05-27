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
    


def play_game():
    """
    A function to control the logic
    of Camel Cards.
    """
    inputs = split_input_string("inputs.txt")
    print(inputs)


if __name__ == "__main__":
    play_game()
