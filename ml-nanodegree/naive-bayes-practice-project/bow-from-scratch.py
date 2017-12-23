# Bag of Words algorithm written from scratch example

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

lower_case_documents = []
for doc in documents:
    lower_case_documents.append(doc.lower())

import string
sans_punctuation_documents = []
for doc in lower_case_documents:
    sans_punctuation_documents.append(doc.translate(str.maketrans('', '', string.punctuation)))

preprocessed_documents = []
for doc in sans_punctuation_documents:
    preprocessed_documents.append(doc.split(" "))

import collections
frequency_list = []
for bag in preprocessed_documents:
    frequency_list.append(collections.Counter(bag))

print(frequency_list)
