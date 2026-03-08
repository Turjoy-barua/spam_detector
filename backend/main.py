import pandas as pd
import joblib
import sklearn
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import api
model = joblib.load("/Users/turjoybarua/Documents/spam_detector/backend/spam_model.joblib")
vectorizer = joblib.load("/Users/turjoybarua/Documents/spam_detector/backend/tfidf_vectorizer.joblib")
   
def mail_input(text_input):
    text_input_vectorized = vectorizer.transform([text_input])
    prediction = model.predict(text_input_vectorized)
    prediction_proba = model.predict_proba(text_input_vectorized)

    if prediction == [1]:
        print("this is a spam mail")
    else:
        print("this is a ham mail")
    
    
    words = vectorizer.get_feature_names_out()
    coeff = model.coef_[0]
    non_zero_idx = words.nonzero()

    df_email = pd.DataFrame({
        "word": words[non_zero_idx],
        "tfidf": text_input_vectorized.toarray()[0][non_zero_idx],
        "coef": coeff[non_zero_idx]
    })

    df_email["impact"] = (df_email["tfidf"] * df_email["coef"]) * 100

    if prediction == [1]:
        df_email = df_email.sort_values("impact", ascending=False)
    else:
        df_email = df_email.sort_values("impact")
            



    return prediction,prediction_proba,df_email.head(10)

#prediction, prediction_proba, words = mail_input('''Subject: CONGRATULATIONS!!! YOU WON $1,000,000!!!
#You have been selected as the lucky winner of $1,000,000!
#Click here immediately to claim your prize before it expires!!!''')
#print(prediction_proba[0][1])
#print(words.loc(1))
