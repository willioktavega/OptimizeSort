import random
import csv

def create_file(filename, amount):
# filename = 'input/age7000.txt'
# if __name__ == '__main__':
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for i in range(amount):
            # [random.randint(1, 80)]
            writer.writerow([random.randint(1, 80)])