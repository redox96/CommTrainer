def topflop_output(topFive):
    string_all = ""
    for i in range(5):
        row_now = topFive[i]
        topTuple = tuple(row_now)
        string_out = "%s %ss (%s)  " % topTuple
        string_all = string_all+string_out
        #print(string_all)

    return string_all


#top_output([['LX', 25.42, '1'], ['KM', 22.01, '6'], ['FS', 19.44, '1'], ['WU', 19.38, '3'], ['WH', 17.0, '1']])


