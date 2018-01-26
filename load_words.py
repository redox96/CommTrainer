import csv

def show_words(letterpair, buffer):
    tot_num = 24 - len(buffer)
    if type == "Corner":
        total = tot_num*(tot_num-1)-21
    elif type == "Edge":
        total = tot_num*(tot_num-1)-22
    else:
        total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        for i in range(0,total):
            if words[i][0] == str(letterpair):
                words_out = words[i][1]
                #print(words_out)
                return str(words_out)
            else:
                pass

def show_words2(letterpair, buffer):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        for i in range(0,total):
            if words[i][0] == str(letterpair):
                adjs_out = words[i][2]
                return str(adjs_out)
            else:
                pass

def show_words3(letterpair, buffer):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        for i in range(0,total):
            if words[i][0] == str(letterpair):
                verbs = words[i][3]
                return str(verbs)
            else:
                pass



#res = show_words("AB", ["A","E","R"])
#print(res)
#print(type(res))
