import csv
import random


def choosingrand():
    number = []
    taketh = []
    for i in range(9):
        with open(f"newmovies{i}.csv", "r", encoding='utf-8', newline = '') as csvfile:
            file = csv.reader(csvfile)
            for row in file:
                binary = row[slice(5,6)]
                direct = row[slice(21,25,3)]
                number.append([binary, direct])
        print(len(number))
        for j in range(10):
            taketh.append(random.randint(0, len(number)))
            print(f"From newmovies{i}, we have {taketh[j]}: {number[taketh[j]]}")
        number = []
    return taketh

choosingrand()
