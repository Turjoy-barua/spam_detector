import pandas as pd
import joblib
import sklearn
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import api
model = joblib.load("spam_model.joblib")
vectorizer = joblib.load("tfidf_vectorizer.joblib")
   
def mail_input(text_input):
    text_input_vectorized = vectorizer.transform([text_input]) # transforming the words 
    prediction = model.predict(text_input_vectorized)   # using the same model to predict
    prediction_proba = model.predict_proba(text_input_vectorized) # to get the probability of being spam and ham 

    if prediction == [1]: # just to check in terminal if needed
        print("this is a spam mail")
    else:
        print("this is a ham mail")
    
    
    words = vectorizer.get_feature_names_out()
    coeff = model.coef_[0]
    non_zero_idx = words.nonzero()

    df_email = pd.DataFrame({ # to get the list of words that affects the mail 
        "word": words[non_zero_idx],
        "tfidf": text_input_vectorized.toarray()[0][non_zero_idx],
        "coef": coeff[non_zero_idx]
    })

    df_email["impact"] = (df_email["tfidf"] * df_email["coef"]) * 100

    if prediction == [1]: # for being spam or ham
        df_email = df_email.sort_values("impact", ascending=False)
    else:
        df_email = df_email.sort_values("impact")
            



    return prediction,prediction_proba,df_email.head(10)

#prediction, prediction_proba, words = mail_input('''Subject: CONGRATULATIONS!!! YOU WON $1,000,000!!!
#You have been selected as the lucky winner of $1,000,000!
#Click here immediately to claim your prize before it expires!!!''')
#print(prediction_proba[0][1])
#print(words.loc(1))
