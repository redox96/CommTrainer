import random
#from group_for_randomization import group_for_rand

#comms_groups = group_for_rand(7, "Corner")

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

    if len(repeaters) > 0:
        dist = ["R", "R", "R", "R", "R", "R", "R", "R", "SN", "SN"]
        pran_comm = random.choice(dist)
        #print(pran_comm)
    else:
        if len(new) > 0:
            dist = ["N", "N", "N", "N", "S", "S", "S", "S", "S", "S"]
            pran_comm = random.choice(dist)
            #print(pran_comm)
        else:
            dist = ["B", "B", "B", "B", "B", "B", "B", "O", "O", "L"]
            pran_comm = random.choice(dist)
            #print(pran_comm)

    if pran_comm == "N":
        comm = random.choices(new, new_weight)
        #print(comm)
    elif pran_comm == "B":
        comm = random.choices(bad, bad_weight)
        #print(comm)
    elif pran_comm == "O":
        comm = random.choices(old, old_weight)
        #print(comm)
    elif pran_comm == "R":
        comm = random.choices(repeaters, repeaters_weight)
        print(comm)
    elif pran_comm == "L":
        comm = random.choices(rest, rest_weight)
        #print(comm)
    elif pran_comm == "S":
        len_all = len(bad)+len(old)+len(rest)
        rels = [len(bad)/len_all, len(old)/len_all, len(rest)/len_all]
        rand_choice_type = random.choices(["bad", "old", "rest"], rels)
        #comm = random.choices("%s"%(rand_choice_type), "%s_weight"%(rand_choice_type))

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
        #print(rand_choice_type)
        #print(type(rand_choice_type))

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

#comm_chooser(comms_groups)
