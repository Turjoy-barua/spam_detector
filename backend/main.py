import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import joblib

import api

def mail_input(text_input):
    model = joblib.load("/Users/TURJOY/Documents/spam_detector/backend/spam_model.joblib")
    vectorizer = joblib.load("backend/tfidf_vectorizer.joblib")
    text_input_vectorized = vectorizer.transform([text_input])
    prediction = model.predict(text_input_vectorized)
    prediction_proba = model.predict_proba(text_input_vectorized)

    if prediction == [1]:
        print("this is a spam mail")
    else:
        print("this is a ham mail")
    print(prediction)
    print(prediction_proba)
    
    return prediction,prediction_proba


print(api.get_mail())
mail_input(api.get_mail())