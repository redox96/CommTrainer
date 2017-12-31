import csv

def group_for_rand(cutoff, type):
    oldness = 100

    # get repeaters
    with open ("data/output_test_%s.csv"%(type), "r", newline="") as letterlist:
        reader = csv.reader(letterlist)
        results_output = list(reader)
        new = []
        repeaters = []
        bad = []
        old = []
        rest = []
        new_weights = []
        repeaters_weights = []
        bad_weights = []
        old_weights = []
        rest_weights = []

        for i in range(len(results_output)):
            if int(results_output[i][2]) == 0:
                new.append(results_output[i][0])
                new_weights.append(1)
                #print(new)
            elif int(results_output[i][2]) > 0 and int(results_output[i][2]) < 2:
                # Store letterpairs of repeaters
                index_last = int(results_output[i][3])-1
                count = int(results_output[i][2])
                repeaters.append(results_output[i][0])
                repeaters_weights.append(index_last/(2**count))
                #print(repeaters)
            elif float(results_output[i][1]) > cutoff:
                bad.append(results_output[i][0])
                bad_weights.append(float(results_output[i][1])**(1.2))
                #print(bad)
            elif int(results_output[i][2]) > oldness:
                old.append(results_output[i][0])
                old_weights.append(float(results_output[i][2])**(1.2))
                #print(old)
            else:
                rest.append(results_output[i][0])
                rest_weights.append(float(results_output[i][1])+float(results_output[i][2])**1.2)
                #print(rest)

        #print(len(bad),len(bad))
        return new, new_weights, repeaters, repeaters_weights, bad, bad_weights, old, old_weights, rest, rest_weights

#print(group_for_rand(7, "Corner")[2])
#print(group_for_rand(7, "Corner")[2])
