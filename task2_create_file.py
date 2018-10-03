import random

def create_file(filename, amount):
    with open(filename, 'w') as file:
        for i in range(amount):
            file.write(str(random.randint(1, 80)))
            file.write('\n')