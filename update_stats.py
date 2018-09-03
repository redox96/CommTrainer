import csv

def update_stats(randlet, d_time, buffer, type):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-42
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    with open ("data/average_%s.csv"%(type), "r", newline="") as buffers:
        reader = csv.reader(buffers)
        bufferavrgs = list(reader)

        with open ("data/output_%s.csv"%(type), "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            letterlist_int = list(reader)

            for i in range(0,total):
                if letterlist_int[i][0] == randlet:
                    bufferavrgs[i][1] = float(bufferavrgs[i][2])
                    bufferavrgs[i][2] = float(bufferavrgs[i][3])
                    bufferavrgs[i][3] = float(bufferavrgs[i][4])
                    bufferavrgs[i][4] = float(bufferavrgs[i][5])
                    bufferavrgs[i][5] = d_time
                    bufferbox = [bufferavrgs[i][1], bufferavrgs[i][2], bufferavrgs[i][3], bufferavrgs[i][4], bufferavrgs[i][5]]
                    print(bufferbox)
                    bufferbox_sorted = sorted(bufferbox)
                    print(bufferbox_sorted)
                    bufferbox_sorted.pop(4)
                    bufferbox_sorted.pop(0)
                    print(bufferbox_sorted)
                    bufferbox_average = (bufferbox_sorted[0] + bufferbox_sorted[1] + bufferbox_sorted[2])/3
                    print(bufferbox_average)

                    count = int(letterlist_int[i][2])
                    times_prev = float(letterlist_int[i][1])
                    times_new = (count*times_prev+d_time)/(count+1)

                    letterlist_int[i][2] = count+1
                    letterlist_int[i][1] = times_new
                    letterlist_int[i][5] = bufferbox_average
                    print("ao5", bufferbox_average, bufferbox)

                    with open("data/average_%s.csv"%(type), "w", newline="") as output:
                        writer = csv.writer(output)
                        for val in bufferavrgs:
                            writer.writerow(val)


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

    return [bufferbox_average,count+1] #return times_new for global average


#update_stats("BC", 3.55, ["A", "E", "R"], "Corner")
