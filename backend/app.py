import api
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from main import mail_input  

st.set_page_config(page_title="Spam Detector", page_icon="📧", layout="wide")

# Sidebar

st.sidebar.header("About this App")
st.sidebar.write(
    """
This app detects spam emails using a ML model.
It highlights words that indicate spam and shows the probability.
"""
)
st.sidebar.write("Model: Logistic regression")
st.sidebar.write("Accuracy: 98%")
st.sidebar.write("Dataset: 5171 emails")

st.title("📧 Email Spam Detector", text_alignment="center")

# Top buttons
upper_col1, upper_col2, upper_col3 = st.columns(3)
upper_button1 = upper_col1.button("Paste an email and check it")
upper_button2 = upper_col2.button("Machine Learning model performance")
upper_button3 = upper_col3.button("Check your last mail in inbox")
if "paste_mail" not in st.session_state:
    st.session_state.paste_mail = False
if "api" not in st.session_state:
    st.session_state.api = False
if upper_button1:
    st.session_state.paste_mail = True
    st.session_state.api = False
if upper_button2:
    st.session_state.paste_mail = False
    st.session_state.api =False
if upper_button3:
    st.session_state.paste_mail = False
    st.session_state.api = True


col1, col2 = st.columns([3, 1])  # make input column bigger
# for the mail pasting box
if st.session_state.paste_mail:
        
    email_text = st.text_area("**Enter Email Text Here**", height=500)

    # Analyze Button
    analyze = st.button("Analyze Email")

    if analyze:
        prediction, prediction_proba, words = mail_input(email_text)
        if prediction == 1:
            st.header("This looks like a spam mail")
            prediction_proba = prediction_proba[0][1]
        else:
            st.header("This looks like a ham mail")
            prediction_proba = prediction_proba[0][0]
            
        proba_cont = st.container()
        proba_cont.progress(prediction_proba, text="Probability of spam/ham", width="stretch")
        st.write(words)
        word_freq = dict(zip(words["word"], words["impact"]))
        if not word_freq:
            st.header("no words to generate wordcloud")
        else:
            wordcloud = WordCloud(background_color='white', colormap='coolwarm').generate_from_frequencies(word_freq)

        fig, ax = plt.subplots()
        ax.imshow(wordcloud)
        ax.axis("off")

        st.pyplot(fig)
            
# to show the infos of model
if upper_button2:
    performane_cont = st.container(border=True)
    performane_cont.header("Model: Spam/Ham email classifier v1.0")
    performane_cont.header("type: logistic regression")
    performane_cont.header("dataset: Kaggle")
    performane_cont.header("Training samples: 5171 mails")
    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", "0.98")
    col2.metric("Precision (Class 1)", "0.95")
    col3.metric("Recall (Class 1)", "0.99")
    st.subheader("Confusion matrix")
    st.image("/Users/turjoybarua/Documents/detec_mail_spam/output.png")

# conecting with api and show the last mail 
if st.session_state.api:
    subject, msg = api.get_mail()
    mail_cont = st.container(border=True)
    mail_cont.subheader("Subject: "+subject)
    mail_cont.subheader(msg)
    prediction, prediction_proba, words = mail_input(subject + " " + msg)
    if prediction == 1:
        st.header("This looks like a spam mail")
        prediction_proba = prediction_proba[0][1]
    else:
        st.header("This looks like a ham mail")
        prediction_proba = prediction_proba[0][0]
        
    proba_cont = st.container()
    proba_cont.progress(prediction_proba, text="Probability of spam/ham", width="stretch")
    st.write(words)
    word_freq = dict(zip(words["word"], words["impact"]))
    if not word_freq:
        st.header("no words to generate wordcloud")
    else:
        wordcloud = WordCloud(background_color='white', colormap='coolwarm').generate_from_frequencies(word_freq)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud)
    ax.axis("off")

    st.pyplot(fig)
            