
objet        = ""
mail         = ""
output       = True
output_proba = 1
mots_spam    = ("spam","spam")
def createOutputHTML(output="", output_proba="",mots_spam=""):
    if output == True:
        text2=f"""<h2>SPAM (Probabilité: {output_proba})</h2>
            <h3 id="reasons">Raisons:</h3>
            """
        for mot in mots_spam:
            text2+=f"<p>{mot}</p>"
    else: text2 = "HAM"
    return text2

def showPage(objet="", mail="",output="",output_proba="",mots_spam=""):
    #if mail == "": text1 = "Copier le mail ici"
    #else: 
    text1 = mail
    text2 = createOutputHTML(output,output_proba,mots_spam)
    styles = """
    <style>
        h1 {
          font-family: "Calibri";
          font-size: "50px";
          text-align: center;
          margin-right: 50px
          }
        textarea {
          resize: none;
          font-family: "Calibri";
          font-size: "12px";
        }
        button {
          position:relative;
          top: 30px;
          left: -1500px;
          font-family: "Calibri";
          font-size: "16px";
        }
        input{
          position:relative;
          left: 100px;
          top: 8px;
        }
        label{
          position:relative;
          left: 100px;
          top: 6px;
        }
        div{
          border: 3px solid;
          position:relative;
          top: 30px;
          padding-left: 20px;
        }
        h2{
          font-family: "Calibri";
          font-size: "30px";
          text-align: center;
        }
        h3{
          font-family: "Calibri";
          font-size: "20px";
          text-align: center;
        }
        p{
          font-family: "Calibri";
          font-size: "12px";
        }
    </style>"""
    scripts="""<script>
            function showSlider(){document.getElementById("SliderText").innerHTML = document.getElementById("Slider").value;}
            </script>
            <script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
            <script>
            function detectSpam(){
            sensibility = document.getElementById("Slider").value;
            mail = document.getElementById("mail").value
            $.ajax({
              url: "INSERERSCRIPTPYTHON.py",
             context: document.body
            }).done(function(result) {
                document.getElementById("Result").innerText=result;
            });
            }
            </script> """
    web = f"""
    <html>
        <head>
            <title>Détecteur de Spam</title>
            {styles}
        </head>
        <body>
            <h1>DETECTEUR DE SPAM</h1>
            <textarea rows="30" cols="275" placeholder="Copier le mail ici" id="mail">{text1}</textarea>
            <button type="button" onclick="detectSpam()">Detect</button>
            <input type="range" min="0" max="1" step="0.01" id="Slider" onchange="showSlider()"><label id="SliderText">0.5</label>
            <div id="Result">{text2}</div>
            {scripts}
            <p>­</p>
        </body>
    </html>"""
    print(web)
    file = open("page.html", "w")
    file.write(web)
    file.close()
showPage(objet,mail,output,output_proba,mots_spam)
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