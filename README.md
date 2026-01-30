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

# version française
# Détecteur_de_spam

- L'objectif est d'apprendre à un ordinateur à reconnaître automatiquement les spams grâce à l'apprentissage par l'exemple.

- L'application va entraîner un modèle sur une base de données massive d'emails contenant l'objet, le corps et l'étiquette « spam » ou « non-spam ».

## Fonctionnement
- Extraction des données de la base de données
- Nettoyage et combinaison du corps et de l'objet des données
- Conversion des données en texte à l'aide de TF-IDF
- Entraînement du modèle : 80 % pour l'entraînement, 20 % pour le test → attribution d'une étiquette et d'une probabilité
- Évaluation du modèle à l'aide d'une matrice de confusion → calcul de la précision
- Précision → Rappel → Score F1 → génération du rapport +++ réglage du seuil au-delà de 0,5
- Utilisation de l'interface pour indiquer s'il s'agit d'un spam ou non

## Contenu de l'application

- Champ de saisie : Objet
- Corps de l'email
- Curseur de seuil ou de sensibilité
- Boutons de validation
- Résultats : spam ou non-spam et probabilité
- Affichage des mots clés
- Chargement
- Entraînement ou chargement du modèle
- Carte thermique