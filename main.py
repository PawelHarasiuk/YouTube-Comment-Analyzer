from data_preprocessing import DataPreprocessing
from model import Model
from model_evaluation import ModelEvaluator
from yt_scraper import YTScraper

data_preprocessing = DataPreprocessing()


def prepeare_model():
    X_train_tfidf, X_val_tfidf, y_train, y_val = data_preprocessing.split_data()

    model = Model(X_train_tfidf, y_train)

    model_evaluator = ModelEvaluator(X_val_tfidf, y_val)
    model_metrics = model_evaluator.evaluate_model(model)
    print(model_metrics)
    return model


def rate_yt_comments(url, model):
    try:
        yt_scraper = YTScraper()
        video_id = yt_scraper.extract_video_id(url)
        comments = yt_scraper.get_comments(video_id)

        count_positive = 0
        count_negative = 0
        count_neutral = 0

        for comment in comments:
            vectorized_comment = data_preprocessing.vectorize_text(comment)
            predicted_sentiment = model.predict_sentiment(vectorized_comment)
            if predicted_sentiment == '1':
                print(f"Comment: {comment} | Predicted sentiment: {'positive'}")
                count_positive += 1
            elif predicted_sentiment == '-1':
                print(f"Comment: {comment} | Predicted sentiment: {'negative'}")
                count_negative += 1
            elif predicted_sentiment == '0':
                print(f"Comment: {comment} | Predicted sentiment: {'neutral'}")
                count_neutral += 1

        print(f"Positive comments: {count_positive}")
        print(f"Negative comments: {count_negative}")
        print(f"Neutral comments: {count_neutral}")
        print(f"Positive rate: {count_positive / len(comments) * 100}%")
        print(f"Negative rate: {count_negative / len(comments) * 100}%")
        print(f"Neutral rate: {count_neutral / len(comments) * 100}%")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    model = prepeare_model()

    while True:
        url = input("Enter a YouTube video URL: ")
        rate_yt_comments(url, model)

    # while True:
    #     comment = input("Enter a comment: ")
    #     vectorized_comment = data_preprocessing.vectorize_text(comment)
    #     predicted_sentiment = model.predict_sentiment(vectorized_comment)
    #     if predicted_sentiment == 4:
    #         print(f"Predicted sentiment: {'positive'}")
    #     elif predicted_sentiment == 0:
    #         print(f"Predicted sentiment: {'negative'}")
    #     else:
    #         print(f"Predicted sentiment: {'neutral'}")
