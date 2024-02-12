from sklearn.ensemble import RandomForestClassifier


class Model:

    def __init__(self, X_train, y_train):
        self.X_train, self.y_train = X_train, y_train
        self.classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        self.classifier.fit(X_train, y_train)

    def predict(self, X):
        return self.classifier.predict(X)

    def predict_sentiment(self, text):
        predicted_sentiment = self.classifier.predict(text)
        return predicted_sentiment[0]
