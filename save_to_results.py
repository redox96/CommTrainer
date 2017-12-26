import csv

def save_to_results(randlet, d_time, type):
    if type == "Corner":
        with open("results_Corner.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    elif type == "Edge":
        with open("results_Edge.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    elif type == "Center":
        with open("results_Center.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    elif type == "Wing":
        with open("results_Wing.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    elif type == "Midge":
        with open("results_Midge.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    elif type == "Tcenter":
        with open("results_Tcenter.csv","a", newline="") as fh:
            w = csv.writer(fh)
            w.writerow([randlet, d_time])
    else:
        print("blubb")
