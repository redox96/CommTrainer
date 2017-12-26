import csv

def count_stats2(type):
    with open ("results_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        result_list = list(reader)
        counts_total=len(result_list)
        return counts_total


#cutoff_stats(["A","E","R"],"Corner")
