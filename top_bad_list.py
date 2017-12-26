import csv

def bad_list(buffer,type):
    num_tot = 24 - len(buffer)
    topFiveTimes = [[0]*3 for i in range(num_tot*(num_tot-1))]
    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Edge":
        with open ("output_test_Edge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Center":
        with open ("output_test_Center.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Wing":
        with open ("output_test_Wing.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Midge":
        with open ("output_test_Midge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Tcenter":
        with open ("output_test_Tcenter.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:], reverse=True)
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    else:
        print("Youre superman and dont have any bad comms")

def top_list(buffer,type):
    num_tot = 24 - len(buffer)
    topFiveTimes = [[0]*3 for i in range(num_tot*(num_tot-1))]
    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Edge":
        with open ("output_test_Edge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Center":
        with open ("output_test_Center.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Wing":
        with open ("output_test_Wing.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Midge":
        with open ("output_test_Midge.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    elif type == "Tcenter":
        with open ("output_test_Tcenter.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            topFive = list(reader)
            for i in range(num_tot*(num_tot-1)):
                topFiveTimes[i][1] = round(float(topFive[i][1]),2)
                topFiveTimes[i][0] = topFive[i][0]
                topFiveTimes[i][2] = topFive[i][2]
            topFiveTimes.sort(key=lambda row: row[1:])
            #print(topFiveTimes)
            del topFiveTimes[5:num_tot*(num_tot-1)]
            return topFiveTimes

    else:
        print("You dont have any good comms :(")
