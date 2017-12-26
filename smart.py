import csv

def smart_queue(buffer, type):
    num_tot = 24 - len(buffer)
    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            values = list(reader)
            for i in range(0,num_tot*(num_tot-1)):
                if letterlist_int[i][0] == randlet:
                    count = int(letterlist_int[i][2])
                    times_prev = float(letterlist_int[i][1])
                    times_new = (count*times_prev+d_time)/(count+1)
                    letterlist_int[i][2] = count+1
                    letterlist_int[i][1] = times_new
                else:
                    pass

        with open("output_test_Corner.csv", "w", newline="") as output:
            writer = csv.writer(output)
            for val in letterlist_int:
                writer.writerow(val)

        return [times_new,count]

    elif type == "Edge":
        pass
    
    elif type == "Center":
        pass

    elif type == "Wing":
        pass

    elif type == "Midge":
        pass

    elif type == "Tcenter":
        pass

    else:
        print("Error in smart 'randomization'")


