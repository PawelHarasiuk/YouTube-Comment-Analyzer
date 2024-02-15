from sklearn.metrics import accuracy_score


class ModelEvaluator:
    def __init__(self, X_test, y_test):
        self.X_test = X_test
        self.y_test = y_test

    def evaluate_model(self, model):
        y_pred = model.predict(self.X_test)
        accuracy = round(accuracy_score(self.y_test, y_pred), 4)

        return {
            'Accuracy': accuracy
        }
