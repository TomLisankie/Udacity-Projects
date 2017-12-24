
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