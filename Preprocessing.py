import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("reddit_raw_data.csv")

# Apply sentiment analysis on the 'text' column
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Analyze sentiment distribution
positive = (df['sentiment'] > 0).sum()
neutral = (df['sentiment'] == 0).sum()
negative = (df['sentiment'] < 0).sum()

# Display results
print("Sentiment Analysis Summary:")
print(f"Positive: {positive}, Neutral: {neutral}, Negative: {negative}")
print(f"Proportion (Positive:Neutral:Negative): {positive/len(df):.2%}:{neutral/len(df):.2%}:{negative/len(df):.2%}")

# Pie chart for sentiment proportion
labels = ['Positive', 'Neutral', 'Negative']
sizes = [positive, neutral, negative]
colors = ['green', 'gray', 'red']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Sentiment Proportion")
plt.axis('equal')
plt.show()

# Save preprocessed data
df.to_csv("preprocessed_data.csv", index=False)
