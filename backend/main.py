import pandas as pd
import joblib

import api

def mail_input(text_input):
    model = joblib.load("backend/spam_model.joblib")
    vectorizer = joblib.load("backend/tfidf_vectorizer.joblib")
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

    df_email["impact"] = df_email["tfidf"] * df_email["coef"]

    if prediction == [1]:
        df_email = df_email.sort_values("impact", ascending=False)
    else:
        df_email = df_email.sort_values("impact")
            
    print(df_email.head(5))


    return prediction,prediction_proba



mail_input(["""Dear Valued User,

Congratulations!

Our system has randomly selected your email address as part of the **NovaCloud Loyalty Appreciation Event**. You are eligible to receive a **complimentary premium membership upgrade** and a reward voucher worth **€250**.

However, due to high demand and verification protocols, you must confirm your account within **12 hours**, or your reward will automatically be reassigned to another participant.

To secure your reward, please follow the steps below:

1. Click the secure confirmation link below
   http://novacloud-secure-access.co/verify-user

2. Log in using your email and password for identity verification.

3. Confirm your personal details so we can release your voucher immediately.

Failure to respond promptly may result in permanent cancellation of your reward privileges.

We appreciate your continued participation in our services and hope you enjoy your exclusive benefits.

Sincerely,
NovaCloud Rewards Department
Customer Experience Team

*This is an automated message. Please do not reply directly to this email.*
"""])