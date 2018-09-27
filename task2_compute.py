import time
import csv

# in_file = 'input/age700.txt'
# out_file = 'output/result_age.txt'
def compute_sort(in_file, out_file):
    start_time = time.time()
    dictData = {}
    for i in range(100):
        dictData[i] = []

    with open(in_file, 'r') as f, open(out_file, 'w') as o_file:
        writer = csv.writer(o_file)
        reader = csv.reader(f)

        for i, row in enumerate(reader):
            dictData[int(row[0])].append(int(row[0]))

        for i in dictData:
            if dictData[i] != []:
                [writer.writerow([j]) for j in dictData[i]]

    print("--- %s seconds ---" % (time.time() - start_time))