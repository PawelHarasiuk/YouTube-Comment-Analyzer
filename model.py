from sklearn.linear_model import LogisticRegression


class Model:

    def __init__(self, X_train, y_train):
        self.X_train, self.y_train = X_train, y_train
        self.classifier = LogisticRegression()
        self.classifier.fit(X_train, y_train)

    def predict(self, X):
        return self.classifier.predict(X)

    def predict_sentiment(self, text):
        predicted_sentiment = self.classifier.predict(text)
        return predicted_sentiment[0]
