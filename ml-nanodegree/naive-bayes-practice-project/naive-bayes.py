
import pandas as pd

df = pd.read_table("smsspamcollection/SMSSpamCollection",
                    sep = "\t",
                    header = None,
                    names=["label", "sms_message"])

df['label'] = df.label.map({'ham':0, 'spam':1})

print(df.shape)
print(df.head())

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df["sms_message"], 
                                                    df["label"], 
                                                    random_state=1)

count_vector = CountVectorizer()

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(X_test)

'''
Instructions:

We have loaded the training data into the variable 'training_data' and the testing data into the 
variable 'testing_data'.

Import the MultinomialNB classifier and fit the training data into the classifier using fit(). Name your classifier
'naive_bayes'. You will be training the classifier using 'training_data' and 'y_train' from our split earlier. 
'''

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)

'''
Instructions:
Now that our algorithm has been trained using the training data set we can now make some predictions on the test data
stored in 'testing_data' using predict(). Save your predictions into the 'predictions' variable.
'''

predictions = naive_bayes.predict(testing_data)
print(predictions)