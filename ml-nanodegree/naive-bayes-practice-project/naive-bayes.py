# #read in data and split into lines
# data = open("smsspamcollection/SMSSpamCollection", r).read().splitlines()

# #split each line into components and put those components into dictionary
# smsDict = {}
# for line in data:
#     components = line.split(" ,,, ")
#     smsDict[components[0]] = components[1]

import pandas as pd

df = pd.read_table("smsspamcollection/SMSSpamCollection",
                    sep = "\t",
                    header = None,
                    names=["label", "sms_message"])

df['label'] = df.label.map({'ham':0, 'spam':1})

print(df.shape)
print(df.head())

from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer()