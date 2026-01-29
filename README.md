# spam_detector
- the goal is to teach a computer to recognize spam automatically by learning from examples.
- the app gonna train model on a massive datasheet of email which gonna contain subject, body and label spam or ham
## how it gonna work
- takes data from database
- clean it + combine body and subject
- use tf-idf to covert it into numbers (text)
- train model 80% training 20% test -> gives a label and probability
- evaluate the model using confusing matrix -> gives the accuracy
- precision -> recall -> F1 score -> give the report +++ threshold tuning insted of 0.5 
- uses the interface to say if its spam or not 
## what the app gona contain
- input field: Subject
- email body
- slider threshold or sensitivity
- buttons check 
- results -> spam not spam and probability
- the words that influence 
- loading 
- train model or load model
- image heatmap
