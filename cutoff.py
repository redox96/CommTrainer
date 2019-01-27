import csv

def cutoff_stats(cutoff, buffer, type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-42
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    above_cutoff = 0

    with open ("data/output_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        result_list = list(reader)

        for i in range(0,total-1):
            if float(result_list[i][5]) > cutoff:
                above_cutoff = above_cutoff+1
            else:
                continue

        #print(above_cutoff)
        return above_cutoff


#cutoff_stats(8, ["A","E","R"],"Corner")
