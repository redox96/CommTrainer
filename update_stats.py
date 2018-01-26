import csv

def update_stats(randlet, d_time, buffer, type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-42
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    with open ("data/output_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        letterlist_int = list(reader)
        for i in range(0,total):
            if letterlist_int[i][0] == randlet:
                count = int(letterlist_int[i][2])
                times_prev = float(letterlist_int[i][1])
                times_new = (count*times_prev+d_time)/(count+1)
                letterlist_int[i][2] = count+1
                letterlist_int[i][1] = times_new
            else:
                pass

        with open ("data/results_%s.csv"%(type), "r", newline="") as prev_results:
            reader = csv.reader(prev_results)
            results = list(reader)
            for i in range(0,len(results)):
                for k in range(total):
                    if letterlist_int[k][0]== randlet:
                        ind = len(results)-i
                        letterlist_int[k][3] = ind
                    else:
                        pass

    with open("data/output_%s.csv"%(type), "w", newline="") as output:
        writer = csv.writer(output)
        for val in letterlist_int:
            writer.writerow(val)

    return [times_new,count+1]
