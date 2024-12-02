# Stock Movement Analysis Based on Social Media Sentiment

## Overview
This project analyzes sentiment from Reddit posts in the "stocks" subreddit to predict stock movements. It scrapes posts from Reddit, processes the text data to extract sentiment using TextBlob, and then builds a machine learning model using a RandomForestClassifier to predict whether stock prices will go up or down. The results are visualized using Matplotlib to show the sentiment trends alongside predicted stock movements.

## Project Structure
The project consists of the following scripts:
- **`scraper.py`**: Scrapes data from Reddit and saves it to `reddit_raw_data.csv`.
- **`preprocessing.py`**: Analyzes sentiment and saves the preprocessed data to `preprocessed_data.csv`.
- **`model.py`**: Trains a `RandomForestClassifier` model on the preprocessed data and evaluates its performance.
- **`predict_stock_movement.py`**: Uses the trained model to predict stock movements based on sentiment analysis and visualizes the results.

## Setup

### 1. Clone the repository
```bash
git clone <repository_url>
cd Stock-Movement-Analysis
