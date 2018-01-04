import csv

def show_comm(letterpair, buffer, type):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/comms_%s.csv"%(type), "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        comms = list(reader)
        for i in range(0,total):
            if comms[i][0] == letterpair:
                comm_out = comms[i][1]
                return comm_out
            else:
                pass

