import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


class DataPreprocessing:
    def __init__(self):
        self.df = self.read_data()
        self.tfidf_vectorizer = TfidfVectorizer(max_features=10000)
        self.tfidf_vectorizer.fit(self.df['text'])

    def read_data(self):
        columns = ["text", "category"]
        df = pd.read_csv("../data/Twitter_Data.csv", header=None, names=columns,
                         encoding='ISO-8859-1')
        df = df.dropna(subset=['text', 'category'])
        return df

    def preprocess_text(self, text):
        text = text.lower()
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text

    def split_data(self):
        self.df['text'] = self.df['text'].apply(self.preprocess_text)
        X_train, X_val, y_train, y_val = train_test_split(self.df['text'], self.df['category'], test_size=0.2,
                                                          random_state=42)

        X_train_tfidf = self.tfidf_vectorizer.fit_transform(X_train)
        X_val_tfidf = self.tfidf_vectorizer.transform(X_val)

        return X_train_tfidf, X_val_tfidf, y_train, y_val

    def vectorize_text(self, text):
        preprocessed_text = self.preprocess_text(text)
        vectorized_text = self.tfidf_vectorizer.transform([preprocessed_text])
        return vectorized_text
