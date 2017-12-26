import csv

def recentness(buffer, type):
    tot_num = 24 - len(buffer)

    with open ("data/output_test_%s.csv"%(type), "r", newline="") as output:
        readerOUT = csv.reader(output)
        outputList = list(readerOUT)

        with open ("data/results_%s.csv"%(type), "r", newline="") as prev_results:
            reader = csv.reader(prev_results)
            results = list(reader)
            for i in range(0,len(results)):
                randlet = results[i][0]
                for k in range(tot_num*(tot_num-1)):
                    if outputList[k][0]== randlet:
                        ind = len(results)-i
                        outputList[k][4] = ind
                    else:
                        pass

        with open("data/output_test_%s.csv"%(type), "w", newline="") as output:
            writer = csv.writer(output)
            for val in outputList:
                writer.writerow(val)

    return ind



#recentness([1,2], "Edge")
