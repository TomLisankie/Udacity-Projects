# Bag of Words algorithm written from scikitlearn example

documents = ['Hello, how are you!',
                'Win money, win from home.',
                'Call me now.',
                'Hello, Call hello you tomorrow?']

from sklearn.feature_extraction.text import CountVectorizer

count_vector = CountVectorizer(stop_words = "english")

count_vector.fit(documents)

doc_array = count_vector.transform(documents).toarray()

import pandas as pd
frequency_matrix = pd.DataFrame(doc_array, columns = count_vector.get_feature_names())
print(frequency_matrix)