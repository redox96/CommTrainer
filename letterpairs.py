import random
import string
import csv

def choose_type():
    types = ["Corner", "Edge", "Center", "Wing", "Tcenter", "Midge"]
    return types

def buffer(type):
    if type == "Corner":
        buffers = ["A", "E", "R"]
        return buffers
    elif type == "Edge":
        buffers = ["U", "K"]
        return buffers
    elif type == "Center":
        buffers = ["A"]
        return buffers
    elif type == "Wing":
        buffers = ["U"]
        return buffers
    elif type == "Midge":
        buffers = ["U", "K"]
        return buffers
    elif type == "Tcenter":
        buffers = ["D"]
        return buffers
    else:
        pass

# Create List (letters) with all possible letter pairs
def create_letterpair(buffer):
    tot_num = 24 - len(buffer)
    letters_AX = list(map(chr, range(ord('A'), ord('X')+1)))

    # Remove buffer pieces
    for i in range(24-tot_num):
        letters_AX.remove(buffer[i])

    lett_A = [letter for letter in letters_AX for i in range(tot_num)]
    lett_B = letters_AX*tot_num

    #print(letters_AX)

    # Lett to create letter pairs
    lett = [[0] * 2 for i in range(tot_num*tot_num)]

    # Letters for letterpair, time, counter, fails, last index, weight
    letters = [[0]*6 for i in range(tot_num*tot_num)]

    for i in range(0, tot_num*tot_num-1):
        lett[i][0]= lett_A[i]
        lett[i][1]= lett_B[i]
        letters[i][0] = lett[i][0]+lett[i][1]

    del letters[::(tot_num+1)]
    return(letters)

#letter = create_letterpair(["A","E","R"])

def create_output_file(letters, type):
    with open("output_test_%s.csv"%(type), "w", newline="") as output:
        writer = csv.writer(output)
        for val in letters:
            writer.writerow(val)
    with open("results_%s.csv"%(type), "a", newline="") as results:
        pass

#create_output_file(letter, "Corner")

# Random indexing
def random_LP(buffer, letters):
    tot_num = 24-len(buffer)
    random_ind = random.randint(0, tot_num*(tot_num-1)-1)
    let_pair = letters[random_ind]
    let_pair_only = let_pair[0]
    #print(let_pair_only)
    return let_pair_only

"""
def slowsmart_random_LP(buffer, type):
    num_tot = 24 - len(buffer)
    brandnew = []
    quitenew = []
    learning = []
    torepeat = []
    p_brandnew = 0
    p_quitenew = 0
    p_learning = 0
    p_torepeat = 0
    if type == "Corner":
        with open ("output_test_Corner.csv", "r", newline="") as letterlist:
            reader = csv.reader(letterlist)
            results = list(reader)
            for i in range(num_tot*(num_tot-1)):
                if int(results[i][3]) == 1:
                    brandnew.append(results[i][0])
                elif int(results[i][3]) > 0.85:
                    quitenew.append(results[i][0])
                elif int(results[i][3]) > 0.5:
                    learning.append(results[i][0])
                else:
                    torepeat.append(results[i][0])

        if len(brandnew) == 0:
            p_quitenew = 0.




                to_app = [results[i][0]]*int(results[i][3])
                int_list.append(to_app)
                print(int_list)
            random_letter = random.choice(int_list)
            #print(random_letter)
            return(random_letter)


slowsmart_random_LP([1,2,3], "Corner")
"""
