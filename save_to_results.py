import csv

def save_to_results(randlet, d_time, type):
    with open("data/results_%s.csv"%(type),"a", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([randlet, d_time])
