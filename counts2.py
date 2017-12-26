import csv

def count_stats2(type):
    if type == "Corner":
        with open ("results_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    elif type == "Edge":
        with open ("results_Edge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    elif type == "Center":
        with open ("results_Center.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    elif type == "Wing":
        with open ("results_Wing.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    elif type == "Midge":
        with open ("results_Midge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    elif type == "Tcenter":
        with open ("results_Tcenter.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            result_list = list(reader)
            counts_total=len(result_list)
            return counts_total

    else:
        print("Hm")


#cutoff_stats(["A","E","R"],"Corner")
