def cutoff_motivation(above_cutoff, counts_total):
    if above_cutoff == 0 and counts_total > 2000:
        text = "NICE!! Choose a harder cutoff!"
    elif above_cutoff < 20 and counts_total >10000:
        text = "Du DINO du :)"
    elif above_cutoff < 20 and counts_total >1000:
        text = "Nearly there! You can do it!!"
    elif counts_total > 1000:
        text = "Hang on! There is still a lot to do..."
    elif above_cutoff < 10 and counts_total > 500:
        text = "NICE! But check you have already drilled all the comms"
    elif above_cutoff < 100 and counts_total >500:
        text = "You're getting there!"
    elif above_cutoff < 300 and counts_total >500:
        text = "You definitely need to become more accurate!!"
    elif above_cutoff < 300 and counts_total >200:
        text = "Keep going!"
    elif counts_total > 100:
        text = "Yay, you drilled 100 comms!"
    else:
        text = "Everyone has to start at some point"
    return text
