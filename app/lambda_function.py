import pickle
from fastapi import FastAPI
from data_preprocessing import DataPreprocessing
from yt_scraper import YTScraper
import sys

# app = FastAPI()

model_file = "./app/model.pkl"

with open(model_file, "rb") as f:
    model = pickle.load(f)

data_preprocessing = DataPreprocessing()
url = "https://www.youtube.com/watch?v=CzAyaSolZjY"


# @app.get("/rate_comments/")
def rate_comments():
    try:
        yt_scraper = YTScraper()
        video_id = yt_scraper.extract_video_id(url)
        comments = yt_scraper.get_comments(video_id)

        count_positive = 0
        count_negative = 0
        count_neutral = 0

        sentiment_results = []

        for comment in comments:
            vectorized_comment = data_preprocessing.vectorize_text(comment)
            predicted_sentiment = model.predict_sentiment(vectorized_comment)
            if predicted_sentiment == '1':
                sentiment = 'positive'
                count_positive += 1
            elif predicted_sentiment == '-1':
                sentiment = 'negative'
                count_negative += 1
            elif predicted_sentiment == '0':
                sentiment = 'neutral'
                count_neutral += 1
            sentiment_results.append({"comment": comment, "sentiment": sentiment})

        total_comments = len(comments)
        positive_rate = count_positive / total_comments * 100 if total_comments != 0 else 0
        negative_rate = count_negative / total_comments * 100 if total_comments != 0 else 0
        neutral_rate = count_neutral / total_comments * 100 if total_comments != 0 else 0

        return {
            "positive_comments": count_positive,
            "negative_comments": count_negative,
            "neutral_comments": count_neutral,
            "positive_rate": positive_rate,
            "negative_rate": negative_rate,
            "neutral_rate": neutral_rate,
            "sentiment_results": sentiment_results
        }
    except Exception as e:
        return {"error": str(e)}


print(rate_comments())
