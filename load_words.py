import csv

def show_words(letterpair, buffer):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        #print(words)
        words_out=""
        for i in range(0,total):
            if words[i][0] == letterpair:
                words_out = words[i][1]
                print(words_out)
                return words_out
            else:
                pass

def show_words2(letterpair, buffer):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        #print(words)
        for i in range(0,total):
            if words[i][0] == letterpair:
                adjs_out = words[i][2]
                return adjs_out
            else:
                pass

def show_words3(letterpair, buffer):
    tot_num = 24 - len(buffer)
    total = tot_num*(tot_num-1)

    with open ("data/words.csv", "r", newline="") as intput:
        reader = csv.reader(intput,delimiter =";")
        words = list(reader)
        #print(words)
        for i in range(0,total):
            if words[i][0] == letterpair:
                verbs = words[i][3]
                return verbs
            else:
                pass



res = show_words("AB", ["A","E","R"])
print(res)

