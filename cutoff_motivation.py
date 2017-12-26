def cutoff_motivation(above_cutoff, counts_total):
    if above_cutoff == 0 and counts_total > 2000:
        text = "NICE!! Choose a harder cutoff!"
    elif above_cutoff < 20 and counts_total >10000:
        text = "Du DINO du :)"
    elif above_cutoff < 20 and counts_total >1000:
        text = "Nearly there! You can do it!!"
    elif above_cutoff < 100 and counts_total >500:
        text = "You're getting there!"
    elif above_cutoff < 300 and counts_total >500:
        text = "You definitely need to become more accurate!!"
    elif above_cutoff < 300 and counts_total >200:
        text = "Keep going!"
    else:
        text = "Everyone has to start at some point"
    return text
