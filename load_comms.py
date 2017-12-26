import csv

def show_comm(letterpair, buffer, type):
    num_tot = 24 - len(buffer)
    with open ("data/comms_%s.csv"%(type), "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        comms = list(reader)
        for i in range(0,num_tot*(num_tot-1)):
            if comms[i][0] == letterpair:
                comm_out = comms[i][1]
                return comm_out
            else:
                pass

