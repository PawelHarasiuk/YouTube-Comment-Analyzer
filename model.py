from sklearn.neural_network import MLPClassifier


class NeuralNetwork:

    def __init__(self, X_train, y_train):
        self.X_train, self.y_train = X_train, y_train
        self.classifier = MLPClassifier(solver='lbfgs', random_state=42, max_iter=100, alpha=0.01, hidden_layer_sizes=(30, 30))
        self.classifier.fit(X_train, y_train)