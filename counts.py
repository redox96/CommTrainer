import csv

def count_stats(buffer, type):
    num_tot = 24 - len(buffer)
    counts_total = 0

    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #or .counts for result file
            #print(counts_total)
            return counts_total

    elif type == "Edge":
        with open ("output_test_Edge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #print(counts_total)
            return counts_total

    elif type == "Center":
        with open ("output_test_Center.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #print(counts_total)
            return counts_total

    elif type == "Wing":
        with open ("output_test_Wing.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #print(counts_total)
            return counts_total

    elif type == "Midge":
        with open ("output_test_Midge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #print(counts_total)
            return counts_total

    elif type == "Tcenter":
        with open ("output_test_Tcenter.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                counts_total = counts_total + int(result_list[i][2])

            #print(counts_total)
            return counts_total

    else:
        print("Error in counts")


#cutoff_stats(["A","E","R"],"Corner")
