#To time everything, of course
import csv
import time
start = time.time()
movieyears = []
dataset = ""
title = ""
def readingthedata(giveth):
    with open('movies.csv', "r", encoding='utf-8') as csvfile:
        giveth = csv.reader(csvfile)
        n=0
        for row in giveth:
            movieyears.append(row)
            n+=1
        global title
        title = movieyears[0]
    return movieyears

datainarray = readingthedata(dataset)
print(len(datainarray))

def separatingyears(giveth: list):
    subgroup = []
    taketh = []
    k = 0
    for n in range(len(giveth)):
        if len(subgroup) < 170 and n != len(giveth)-1:
            subgroup.append(giveth[n])
        elif len(subgroup) <180 and n != len(giveth)-1:
            if giveth[n][0] == giveth[n-1][0]:
                subgroup.append(giveth[n])
        else:
            taketh.append(subgroup)
            print(len(taketh))
            k += 1
            subgroup = []
    for i in range(len(taketh)):
        with open(f"newmovies{i}.csv", "w", encoding='utf-8', newline='') as csvfile:
            collecting = csv.writer(csvfile)
            collecting.writerow(title)
            for j in range(len(taketh[i])):
                collecting.writerow(taketh[i][j])

        print(f"Finished with {i}.")
    return taketh

separatingyears(datainarray)

end = time.time()

print(f"Program took {end-start} seconds.")
