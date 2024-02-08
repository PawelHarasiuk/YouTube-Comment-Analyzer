import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


class DataPreprocessing:
    def __init__(self):
        self.df = self.read_data()
        self.tfidf_vectorizer = TfidfVectorizer(max_features=5000)
        self.tfidf_vectorizer.fit(self.df['text'])

    def read_data(self):
        columns = ["sentiment", "timestamp", "date", "query", "user", "text"]
        df = pd.read_csv("data/training.1600000.processed.noemoticon.csv", header=None, names=columns,
                         encoding='ISO-8859-1')
        return df

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text

    def split_data(self):
        self.df['text'] = self.df['text'].apply(self.preprocess_text)
        X_train, X_val, y_train, y_val = train_test_split(self.df['text'], self.df['sentiment'], test_size=0.2,
                                                          random_state=42)
        tfidf_vectorizer = TfidfVectorizer(max_features=5000)

        X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
        X_val_tfidf = tfidf_vectorizer.transform(X_val)

        return X_train_tfidf, X_val_tfidf, y_train, y_val

    def vectorize_text(self, text):
        preprocessed_text = self.preprocess_text(text)
        vectorized_text = self.tfidf_vectorizer.transform([preprocessed_text])
        return vectorized_text

