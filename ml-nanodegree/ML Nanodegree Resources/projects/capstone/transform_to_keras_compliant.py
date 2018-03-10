import pandas as pd 
import numpy as np
import csv

np.random.seed(172632)

train = pd.read_csv("capstone_train_and_test/train.csv")
test = pd.read_csv("capstone_train_and_test/test.csv")

phonemes_to_int_reference = {}
with open('phonemes_to_int.csv', mode='r') as nemes:
    reader = csv.reader(nemes)
    for k,v in reader:
        phonemes_to_int_reference[k] = v

def translate_phonemes_to_ints(phoneme_string):
    phoneme_list = phoneme_string.split(" ")
    int_list = [phonemes_to_int_reference[p] for p in phoneme_list]
    int_string = " ".join(int_list)
    return int_string

def floor_rhyme_percentile(rp):
    floored = math.floor(float(rp)*10)/10
    return floored

transformed_train = pd.DataFrame(columns = 
                    ["phonemic_transcriptions_1", "phonemic_transcriptions_2", "rhyme_percentile"])
transformed_test = pd.DataFrame(columns = 
                    ["phonemic_transcriptions_1", "phonemic_transcriptions_2", "rhyme_percentile"])

for old_row in train.iloc[:, 0:0].values:
    new_row = pd.Series([translate_phonemes_to_ints(old_row[0]), translate_phonemes_to_ints(old_row[1]), 
                floor_rhyme_percentile(old_row[2])])
    transformed_train.append(new_row)

print(transformed_train)
    

