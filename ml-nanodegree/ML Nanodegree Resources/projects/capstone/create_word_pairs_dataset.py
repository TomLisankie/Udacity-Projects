import pandas as pd 
import numpy as np

np.random.seed(172632)

# read transcriptions
phonemic_transcriptions_frame = pd.read_csv("just_transcriptions.csv")
phonemic_transcriptions_list = phonemic_transcriptions_frame.iloc[:, :].values
reg_list = list(phonemic_transcriptions_list)

# for loops to pair them all up
pairs_list = []
for phonemic_trans1 in reg_list:
    for phonemic_trans2 in reg_list:
        pairs_list.append([phonemic_trans1[0], phonemic_trans2[0]])
    #remove first element in reg_list so there aren't any duplicates later on
    reg_list.pop(0)

# TODO: find rhyme percentile for each pair of words

# shuffle
import random
random.seed(172632)
random.shuffle(pairs_list)
pairs_list.insert(0, ["phonemic_transcriptions_1", "phonemic_transcriptions_2"])

# split into training and testing sets
train = pairs_list[ : int(0.8*len(pairs_list))]
test = pairs_list[int(0.8*len(pairs_list)) : ]

# save train and test sets as CSV files
import csv
with open('train.csv', 'w') as csvfile:
    the_writer = csv.writer(csvfile)
    the_writer.writerows(train)

with open('test.csv', 'w') as csvfile:
    the_writer = csv.writer(csvfile)
    the_writer.writerows(test)