import csv

def cutoff_stats(cutoff, buffer, type):
    num_tot = 24 - len(buffer)
    above_cutoff = 0

    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(0,num_tot*(num_tot-1)-1):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    elif type == "Edge":
        with open ("output_test_Edge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    elif type == "Center":
        with open ("output_test_Center.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    elif type == "Wing":
        with open ("output_test_Wing.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    elif type == "Midge":
        with open ("output_test_Midge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    elif type == "Tcenter":
        with open ("output_test_Tcenter.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)

            for i in range(num_tot*(num_tot-1)):
                if float(result_list[i][1]) > cutoff:
                    above_cutoff = above_cutoff+1
                else:
                    continue

            print(above_cutoff)
            return above_cutoff

    else:
        print("Did you choose a cutoff?")


#cutoff_stats(8, ["A","E","R"],"Corner")
