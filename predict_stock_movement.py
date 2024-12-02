import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load preprocessed data
df = pd.read_csv("preprocessed_data.csv")

# Apply sentiment analysis on the 'text' column if not already done
if 'sentiment' not in df.columns:
    df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Predict stock movements using the trained model
df['predicted_movement'] = model.predict(df[['sentiment']])

# Convert 'created_utc' to datetime if not already
df['created_utc'] = pd.to_datetime(df['created_utc'])

# Plot trends
plt.figure(figsize=(10, 6))
plt.plot(df['created_utc'], df['sentiment'], label="Sentiment Polarity", color="blue")
plt.scatter(df['created_utc'], df['predicted_movement'], label="Predicted Movement", color="orange", alpha=0.6)
plt.title("Sentiment Polarity vs. Predicted Stock Movement")
plt.xlabel("Date")
plt.ylabel("Sentiment Polarity / Movement")
plt.legend()
plt.grid(True)
plt.show()
