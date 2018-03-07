import pandas as pd
import numpy as np

np.random.seed(172632)
phonemic_transcriptions_frame = pd.read_csv("phonemic_transcriptions.csv")
print(phonemic_transcriptions_frame.shape)
# phonemic_transcriptions_list = phonemic_transcriptions_frame.iloc[0].values
# shuffled = np.random.shuffle(phonemic_transcriptions_list)
# print(shuffled)
