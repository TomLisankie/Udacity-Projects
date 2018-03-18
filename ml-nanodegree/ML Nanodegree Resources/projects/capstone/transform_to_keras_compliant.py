import pandas as pd 
import numpy as np
import csv
import math

np.random.seed(172632)

train = pd.read_csv("capstone_train_and_test/old_train.csv")
test = pd.read_csv("capstone_train_and_test/old_test.csv")

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

transformed_train["phonemic_transcriptions_1"] = pd.Series([translate_phonemes_to_ints(sequence) for sequence in train["phonemic_transcriptions_1"]])
transformed_train["phonemic_transcriptions_2"] = pd.Series([translate_phonemes_to_ints(sequence) for sequence in train["phonemic_transcriptions_2"]])
transformed_train["rhyme_percentile"] = pd.Series([floor_rhyme_percentile(rp) for rp in train["rhyme_percentile"]])

transformed_test["phonemic_transcriptions_1"] = pd.Series([translate_phonemes_to_ints(sequence) for sequence in test["phonemic_transcriptions_1"]])
transformed_test["phonemic_transcriptions_2"] = pd.Series([translate_phonemes_to_ints(sequence) for sequence in test["phonemic_transcriptions_2"]])
transformed_test["rhyme_percentile"] = pd.Series([floor_rhyme_percentile(rp) for rp in test["rhyme_percentile"]])

transformed_train.to_csv("capstone_train_and_test/final_train.csv", index = False)
transformed_test.to_csv("capstone_train_and_test/final_test.csv", index = False)