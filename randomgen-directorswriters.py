import csv
import random


def choosingrand():
    number = []
    taketh = []
    finalized = []
    for i in range(10):
        with open(f"newmovies{i}.csv", "r", encoding='utf-8', newline = '') as csvfile:
            taketh = []
            file = csv.reader(csvfile)
            for row in file:
                binary = row[slice(5,6)]
                direct = row[slice(21,25,3)]
                number.append([binary, direct])
        print(len(number))
        for j in range(10):
            taketh.append(random.randint(1, len(number)-1))
            finalized.append([taketh[j],number[taketh[j]]])
            print(f"From newmovies{i}, we have {taketh[j]}: {number[taketh[j]]}")
        number = []
    return finalized

data = choosingrand()
with open("randdata.txt", mode='a', encoding="utf-8") as file:
    file.write(f"{data}")
