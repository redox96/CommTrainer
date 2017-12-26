import csv

def count_stats(buffer, type):
    num_tot = 24 - len(buffer)
    counts_total = 0

    with open ("output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        result_list = list(reader)

        for i in range(num_tot*(num_tot-1)):
            counts_total = counts_total + int(result_list[i][2])

        return counts_total


