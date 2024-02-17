import pickle
from data_preprocessing import DataPreprocessing
from model_evaluation import ModelEvaluator
from model import Model

model_file = "./model.pkl"


def prepeare_model():
    data_preprocessing = DataPreprocessing()
    X_train_tfidf, X_val_tfidf, y_train, y_val = data_preprocessing.split_data()

    model = Model(X_train_tfidf, y_train)

    model_evaluator = ModelEvaluator(X_val_tfidf, y_val)
    model_metrics = model_evaluator.evaluate_model(model)
    print(model_metrics)
    return model


with open(model_file, "wb") as f:
    model = prepeare_model()
    pickle.dump(model, f)
