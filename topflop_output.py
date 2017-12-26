def topflop_output(topFive):
    string_all = ""
    for i in range(5):
        row_now = topFive[i]
        topTuple = tuple(row_now)
        string_out = "%s %ss (%s)  " % topTuple
        string_all = string_all+string_out
        #print(string_all)

    return string_all

