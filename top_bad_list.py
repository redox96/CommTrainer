import csv

def bad_list(buffer,type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-21
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    topFiveTimes = [[0]*3 for i in range(total)]

    with open ("data/output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        topFive = list(reader)
        for i in range(total):
            topFiveTimes[i][1] = round(float(topFive[i][1]),2)
            topFiveTimes[i][0] = topFive[i][0]
            topFiveTimes[i][2] = topFive[i][2]
        topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
        #print(topFiveTimes)
        del topFiveTimes[5:total]
        return topFiveTimes


def top_list(buffer,type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-21
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    topFiveTimes = [[0]*3 for i in range(total)]

    with open ("data/output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        topFive = list(reader)
        for i in range(total):
            topFiveTimes[i][1] = round(float(topFive[i][1]),2)
            topFiveTimes[i][0] = topFive[i][0]
            topFiveTimes[i][2] = topFive[i][2]
        topFiveTimes.sort(key=lambda row: row[1:])
        #print(topFiveTimes)
        del topFiveTimes[5:total]
        return topFiveTimes

