import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
import os

def train_model():
    # Load the dataset
    df = pd.read_csv("data/prompts.csv")
    X = df["prompt"]           # Input text (prompts)
    y = df["label"]            # Labels: safe or malicious

    # Create a pipeline: text vectorizer + classifier
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    # Train the model
    pipeline.fit(X, y)

    # Save the trained model
    os.makedirs("model", exist_ok=True)
    joblib.dump(pipeline, "model/prompt_detector.pkl")
    print("Model saved to model/prompt_detector.pkl")

# Run the training function
if __name__ == "__main__":
	train_model()
