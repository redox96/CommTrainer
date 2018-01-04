import csv

def count_stats(buffer, type):
    tot_num = 24 - len(buffer)

    if type == "Corner":
        total = tot_num*(tot_num-1)-21 #minus twists
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22 #minus flips
    else:
        total = tot_num*(tot_num-1)

    counts_total = 0

    with open ("data/output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        result_list = list(reader)

        for i in range(total):
            counts_total = counts_total + int(result_list[i][2])

        return counts_total


