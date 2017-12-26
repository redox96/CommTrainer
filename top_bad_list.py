import csv

def bad_list(buffer,type):
    num_tot = 24 - len(buffer)
    topFiveTimes = [[0]*3 for i in range(num_tot*(num_tot-1))]

    with open ("output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        topFive = list(reader)
        for i in range(num_tot*(num_tot-1)):
            topFiveTimes[i][1] = round(float(topFive[i][1]),2)
            topFiveTimes[i][0] = topFive[i][0]
            topFiveTimes[i][2] = topFive[i][2]
        topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
        #print(topFiveTimes)
        del topFiveTimes[5:num_tot*(num_tot-1)]
        return topFiveTimes


def top_list(buffer,type):
    num_tot = 24 - len(buffer)
    topFiveTimes = [[0]*3 for i in range(num_tot*(num_tot-1))]

    with open ("output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        topFive = list(reader)
        for i in range(num_tot*(num_tot-1)):
            topFiveTimes[i][1] = round(float(topFive[i][1]),2)
            topFiveTimes[i][0] = topFive[i][0]
            topFiveTimes[i][2] = topFive[i][2]
        topFiveTimes.sort(key=lambda row: row[1:])
        #print(topFiveTimes)
        del topFiveTimes[5:num_tot*(num_tot-1)]
        return topFiveTimes

