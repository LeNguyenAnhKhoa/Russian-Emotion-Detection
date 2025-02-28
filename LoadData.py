import pandas as pd
import numpy as np
from PreprocessData import preprocess_russian_text

def map_emotion(row):
    x = [0, 0, 0, 0, 0, 0]
    if row['anger'] == 1:
        x[0] = 1
    if row['disgust'] == 1:
        x[1] = 1
    if row['fear'] == 1:
        x[2] = 1
    if row['joy'] == 1:
        x[3] = 1
    if row['sadness'] == 1:
        x[4] = 1
    if row['surprise'] == 1:
        x[5] = 1
    return x

def load_dataset(train_path, test_path):
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
        
    train_df['text'] = train_df['text'].apply(preprocess_russian_text)
    test_df['text'] = test_df['text'].apply(preprocess_russian_text)
        
    train_df['labels'] = train_df.apply(map_emotion, axis=1)
    train_df = train_df.drop(['anger', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'id'], axis=1)
        
    X = np.array(train_df['text'])
    y = train_df['labels']
    X_test = np.array(test_df['text']).tolist()
        
    return X, y, X_test, test_df