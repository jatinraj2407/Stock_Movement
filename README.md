# Stock Movement Analysis Based on Social Media Sentiment

## Overview
This project analyzes sentiment from Reddit posts in the "stocks" subreddit to predict stock movements. The goal is to use machine learning models to forecast stock price trends based on social media sentiment.

---

## Setup

### 1. Clone the Repository
To begin, clone the repository to your local machine using Git. This will download the project files.

```bash
git clone <repository_url>
cd Stock-Movement-Analysis
```

Replace `<repository_url>` with the actual URL of your GitHub repository.

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to avoid conflicts with other Python projects or global packages. Follow these steps to create and activate the virtual environment:

1. **Create a Virtual Environment**:
   - On **Windows**:
     ```bash
     python -m venv venv
     ```
   - On **macOS/Linux**:
     ```bash
     python3 -m venv venv
     ```

2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

---

### 3. Install Dependencies
Once the virtual environment is set up, you need to install all the required libraries. This can be done easily by running the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary libraries listed in the `requirements.txt` file, which includes:
- `pandas`
- `praw`
- `textblob`
- `scikit-learn`
- `matplotlib`

---

### 4. Reddit API Credentials
Before running the scraper, you will need to set up Reddit API credentials. To do this:

1. Go to the [Reddit API page](https://www.reddit.com/prefs/apps) and create a new application.
2. Note the `client_id`, `client_secret`, and `user_agent` provided after the application is created.
3. Replace these credentials in the `scraper.py` file to enable access to Reddit data.

```python
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USER_AGENT = "your_user_agent"
```

---

### 5. Running the Code

#### **1. Scraping Reddit Data (`scraper.py`)**
The first step is to scrape Reddit posts from the "stocks" subreddit. This script collects the titles, scores, comments, creation dates, and text of Reddit posts and saves them to a CSV file.

To run the scraper, execute the following command:

```bash
python scraper.py
```

The scraped data will be saved in a file named `reddit_raw_data.csv`.

#### **2. Preprocessing Data (`preprocessing.py`)**
This script processes the scraped data by performing sentiment analysis on the text of the Reddit posts. The sentiment score (polarity) is calculated using TextBlob, and the results are saved to `preprocessed_data.csv`.

To run the preprocessing script:

```bash
python preprocessing.py
```

#### **3. Training the Model (`model.py`)**
This script trains a machine learning model using a Random Forest Classifier to predict stock movement based on sentiment analysis.

To train the model:

```bash
python model.py
```

After training, the model is saved and ready for use in prediction.

#### **4. Predicting Stock Movement (`predict_stock_movement.py`)**
This script uses the trained model to predict stock movements based on the sentiment scores. It visualizes the sentiment vs. predicted stock movements over time.

To run the prediction script:

```bash
python predict_stock_movement.py
```

---

## File Descriptions

- **`scraper.py`**: Scrapes data from Reddit and saves it to `reddit_raw_data.csv`.
- **`preprocessing.py`**: Analyzes sentiment of Reddit posts and saves the preprocessed data to `preprocessed_data.csv`.
- **`model.py`**: Trains a RandomForestClassifier model and evaluates its performance on predicting stock movements.
- **`predict_stock_movement.py`**: Uses the trained model to predict stock movements and visualizes the results.

---

## Future Improvements

- **Integrating Multiple Data Sources**: Expand the project by collecting data from additional social media platforms like Twitter or Telegram.
- **Improved Sentiment Analysis**: Explore more advanced sentiment analysis techniques using NLP models such as BERT for more accurate predictions.
- **Real-time Data**: Modify the scraper to collect data in real time and update predictions continuously.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Points in the README:
- **Clone the Repository**: Instructions for cloning the repo and navigating to the project directory.
- **Setting Up the Virtual Environment**: Guide to creating and activating a virtual environment.
- **Installing Dependencies**: Step to install all necessary libraries via the `requirements.txt` file.
- **Reddit API Credentials**: Instructions to set up Reddit API credentials and use them in the code.
- **Running the Code**: Step-by-step guide on running the individual scripts for data collection, preprocessing, model training, and prediction.
- **File Descriptions**: A summary of what each Python script does in the project.
- **Future Improvements**: Ideas for expanding and improving the project.
- **License**: Information about the open-source license.

---

This README should provide clear instructions to set up, run, and understand the project. Let me know if you need any more additions!
