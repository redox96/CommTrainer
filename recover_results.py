import csv

def recover_results(buffer, type):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/output_test_%s.csv"%(type), "r", newline="") as output:
        readerOUT = csv.reader(output)
        outputList = list(readerOUT)

        with open ("data/results_%s.csv"%(type), "r", newline="") as prev_results:
            reader = csv.reader(prev_results)
            results = list(reader)
            for i in range(0,len(results)):
                randlet = results[i][0]
                d_time = float(results[i][1])
                for k in range(total):
                    if outputList[k][0]== randlet:
                        count = int(outputList[k][2])
                        times_prev = float(outputList[k][1])
                        times_new = (count*times_prev+d_time)/(count+1)
                        outputList[k][2] = count+1
                        outputList[k][1] = times_new
                        if d_time > 15:
                            outputList[k][4]= int(outputList[k][4])+1
                        else:
                            pass
                    else:
                        pass
                    if outputList[k][0]== randlet:
                        ind = len(results)-i
                        outputList[k][3] = ind
                    else:
                        pass

        with open("data/output_test_%s.csv"%(type), "w", newline="") as output:
            writer = csv.writer(output)
            for val in outputList:
                writer.writerow(val)

#recover_results(["A","E","R"], "Corner")
