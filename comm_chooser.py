import random

def comm_chooser(comms_groups):
    new = comms_groups[0]
    new_weight = comms_groups[1]
    repeaters = comms_groups[2]
    repeaters_weight = comms_groups[3]
    bad = comms_groups[4]
    bad_weight = comms_groups[5]
    old = comms_groups[6]
    old_weight = comms_groups[7]
    rest = comms_groups[8]
    rest_weight = comms_groups[9]

    #print(repeaters_weight)
    #print(len(repeaters_weight), len(repeaters))

    if len(new) > len(new)+len(repeaters)+len(bad)+len(old)+len(rest)-5:
        pran_comm = "N"

    elif len(repeaters) > 5:
        dist = ["R", "R", "R", "R", "R", "R", "R", "R", "SN", "SN"]
        pran_comm = random.choice(dist)

    else:
        if len(new) > 0:
            dist = ["N", "N", "N", "N", "S", "S", "S", "S", "S", "S"]
            pran_comm = random.choice(dist)

        else:
            dist = ["B", "B", "B", "B", "B", "B", "B", "O", "O", "L"]
            pran_comm = random.choice(dist)

    if pran_comm == "N":
        comm = random.choices(new, new_weight)
    elif pran_comm == "B":
        comm = random.choices(bad, bad_weight)
    elif pran_comm == "O":
        comm = random.choices(old, old_weight)
    elif pran_comm == "R":
        comm = random.choices(repeaters, repeaters_weight)
    elif pran_comm == "L":
        comm = random.choices(rest, rest_weight)
    elif pran_comm == "S":
        len_all = len(bad)+len(old)+len(rest)
        rels = [len(bad)/len_all, len(old)/len_all, len(rest)/len_all]
        rand_choice_type = random.choices(["bad", "old", "rest"], rels)

        if rand_choice_type[0] == "bad":
            comm = random.choices(bad, bad_weight)
            print(comm)
        elif rand_choice_type[0] == "old":
            comm = random.choices(old, old_weight)
            print(comm)
        elif rand_choice_type[0] == "rest":
            comm = random.choices(rest, rest_weight)
            print(comm)
        else:
            print("Error S")
        print(comm)

    elif pran_comm == "SN":
        len_all = len(new)+len(bad)+len(old)+len(rest)
        rels = [len(new)/len_all, len(bad)/len_all, len(old)/len_all, len(rest)/len_all]
        rand_choice_type = random.choices(["new", "bad", "old", "rest"], rels)

        if rand_choice_type[0] == "new":
            comm = random.choices(new, new_weight)
            print(comm)
        elif rand_choice_type[0] == "bad":
            comm = random.choices(bad, bad_weight)
            print(comm)
        elif rand_choice_type[0] == "old":
            comm = random.choices(old, old_weight)
            print(comm)
        elif rand_choice_type[0] == "rest":
            comm = random.choices(rest, rest_weight)
            print(comm)
        else:
            print("Error SN")
    else:
        print("Error in comm_chooser")

    return comm[0]
