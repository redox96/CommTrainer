import csv

def weigh_comms(buffer, type, cutoff):
    num_tot = 24 - len(buffer)
    c_new = 0
    c_quitenew = 10
    i_ancient = 1000
    min = 1

    with open ("results_%s.csv"%(type), "r", newline="") as list2:
        reader = csv.reader(list2)
        results_collected = list(reader)

        with open ("output_test_%s.csv"%(type), "r", newline="") as letterlist:
            reader2 = csv.reader(letterlist)
            results = list(reader2)

            for i in range(0, num_tot*(num_tot-1)):
                if int(results[i][2]) == c_new:
                    results[i][5] = 1*100 # weight = 1
                elif float(results[i][1]) > cutoff:
                    results[i][5] = 1*100
#                     index_last = len(results_collected) - results_collected[::-1].index(results[i][0]) + 1
                elif int(results[i][2]) in range(1,int(c_quitenew)):
                    results[i][5] = int(round((0.5 + (((float(results[i][1])-min)/(cutoff-min))**2)*0.5)*100,0))
#                     index_last = len(results_collected) - results_collected[::-1].index(results[i][0]) + 1
                else:
                    index_last = len(results_collected) - results_collected[::-1].index(results[i][0]) + 1
                    results[i][3]= index_last
                    if index_last > i_ancient:
                        results[i][5] = int(round((0.3*(index_last/i_ancient)^(1.2) + (((float(results[i][1])-min)/(cutoff-min))**2)*0.7)*100,0))
                    else:
                        results[i][5] = int(round((((float(results[i][1])-min)/(cutoff-min))**2)*100,0))

    with open("output_test_%s.csv"%(type), "w", newline="") as output:
        writer = csv.writer(output)
        for val in results:
            writer.writerow(val)


#weigh_comms([1,2,3], "Corner", 10)
