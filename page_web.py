objet        = ""
mail         = ""
output       = True
output_proba = 1
seuil        = 0.5
mots_spam    = ("spam","spam")

if mail == "": text1 = "Copier le mail ici"
else: text1 = mail
if output == True:
    text2=f"""<h2>SPAM ({output_proba})</h2>
    <h3>Raisons:</h3>
    """
    for mot in mots_spam:
        text2+=f"<p>{mot}</p>"
else: text2 = "HAM"
web = f"""
<html>
    <head>
        <title>Détecteur de Spam</title>
        <styles>
        </styles>
    </head>
    <body>
        <h1>SPAM DETECTOR</h1>
        <td>{text1}</td>
        #insérer bouton et slider ici
        <td>{text2}</td>
    </body>
</html>"""
print(web)
file = open("page.html", "w")
file.write(web)
file.close()
