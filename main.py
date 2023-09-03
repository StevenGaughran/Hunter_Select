import random

def random_hunter_selection():
    my_file = open("hunters.txt", "r")
    data = my_file.read()
    hunter_list = data.split("\n")
    my_file.close()
    selection = random.choice(hunter_list)
    print(selection)

random_hunter_selection()