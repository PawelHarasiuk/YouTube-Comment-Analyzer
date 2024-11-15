# YouTube-Comment-Analyzer

## How this app works 📊
### Description
I developed an application that uses the YouTube Data API to retrieve comments from YouTube, performs sentiment analysis (positive, neutral, negative), and determines the percentage share of each category in the comments. I used Python with libraries such as pandas and scikit-learn for data analysis, as well as JSON format for sending information back to the user. The project is deployed on AWS Lambda, triggered by AWS API Gateway. I managed version control using Git and GitHub, with application packaging in a Docker container.
### Presentation of API using Postman
As you can see in screenshot you send url of youtube video in body and we get back json with analized comments

<img width="850" alt="Zrzut ekranu 2024-02-20 o 18 46 03" src="https://github.com/PawelHarasiuk/YouTube-Comment-Analyzer/assets/96013656/727bbec0-5562-4006-8d59-531630a8dd52">

## Implementation 🐍

### Dataset
The dataset used for this project is sourced from Kaggle, specifically the "Twitter and Reddit Sentimental Analysis Dataset" available at [this link](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset/code). This dataset serves as the foundation for training the sentiment analysis model.

### Technology Used
The project is implemented using the following technologies:
- Python: The primary programming language for developing the YouTube comment evaluator.
- Docker: Used for containerizing the application.
- AWS Lambda: Hosting platform for deploying the Docker image.
- AWS API Gateway: Connects the Lambda function to an API endpoint.
- Pickle: Utilized for serializing the trained model.

## Classification 🔬
### Data Preprocessing
The data preprocessing stage involves cleaning and preparing the dataset for training the model. This includes tasks such as removing irrelevant information, handling missing values, and tokenizing text data.

### Model Used
The sentiment analysis model used in this project is trained on the preprocessed dataset. After training, the model is serialized using Pickle for efficient storage and retrieval. The model is capable of analyzing YouTube comments and determining their sentiment, providing valuable insights into audience reactions.
