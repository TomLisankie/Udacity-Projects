import pandas as pd
import numpy as np

np.random.seed(172632)

# shuffle and shorten
phonemic_transcriptions_frame = pd.read_csv("phonemic_transcriptions.csv")
phonemic_transcriptions_list = phonemic_transcriptions_frame.iloc[:, 1:2].values
np.random.shuffle(phonemic_transcriptions_list)
shuffled_shortened = list(phonemic_transcriptions_list[0 : 5000])

import csv
with open('just_transcriptions.csv', 'w') as csvfile:
    the_writer = csv.writer(csvfile)
    the_writer.writerows(shuffled_shortened)

# create train and test sets
# train = list(shuffled_shortened[:4000])
# test = list(shuffled_shortened[4000:])

# # save train and test sets as CSV files
# import csv
# with open('train.csv', 'w') as csvfile:
#     the_writer = csv.writer(csvfile)
#     the_writer.writerows(train)

# with open('test.csv', 'w') as csvfile:
#     the_writer = csv.writer(csvfile)
#     the_writer.writerows(test)
