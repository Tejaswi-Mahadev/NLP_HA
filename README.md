# NLP HOLIDAY ASSIGMENT 
# Sentimental Analysis on Customer Reviews 

## **Overview**
This notebook performs sentiment analysis on customer reviews from the "Amazon Fine Food Reviews" dataset. It includes exploratory data analysis, preprocessing, and sentiment scoring using both traditional NLP techniques (NLTK) and deep learning models (Roberta).

**Key Concepts**

Data Loading and Preprocessing:

* Fetches the dataset using the Kaggle API.
* Loads and inspects the first 500 reviews for analysis.
  
Exploratory Data Analysis (EDA):

* Visualizes the distribution of review ratings.
* Displays sample reviews for context.
  
Text Preprocessing:

* Tokenizes review text using NLTK.
* Applies POS tagging and named entity recognition (NER).
* 
Sentiment Analysis with NLTK:

* Uses the SentimentIntensityAnalyzer for polarity scoring (positive, neutral, and negative sentiment).
* Combines sentiment scores with the dataset for further analysis.
  
Visualization:

* Analyzes sentiment scores across review ratings.
* Generates bar plots to compare sentiment distributions.
  
Advanced Sentiment Analysis:

* Incorporates a transformer-based model (Roberta) for sentiment scoring.
* Compares NLTK and Roberta sentiment metrics.
* 
Model Comparison:

* Evaluates the outputs of NLTK and Roberta models.
* Highlights significant differences in sentiment predictions.

Pipeline Testing:

* Demonstrates the use of pre-trained sentiment pipelines for standalone analysis.
  
Technologies Used
* Libraries: pandas, matplotlib, seaborn, NLTK, transformers
* Dataset: Amazon Fine Food Reviews (via Kaggle API)
* Models: NLTK's VADER, Roberta (CardiffNLP)
