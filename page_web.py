def createOutputHTML(output:bool="", output_proba:float="",mots_spam:tuple=('',)) -> str:
    "crée le text: Spam/Ham + Raisons"
    if output == True:
        text=f"""<h2>SPAM (Probabilité: {output_proba})</h2>
            <h3 id="reasons">Raisons:</h3>
            """
        for mot in mots_spam:
            text2+=f"<p>{mot}</p>"
    else: text = "HAM"
    return text

def createPage() -> str:
    "Crée la page web"
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
            <textarea rows="30" cols="275" placeholder="Copier le mail ici" id="mail"></textarea>
            <button type="button" onclick="detectSpam()">Detect</button>
            <input type="range" min="0" max="1" step="0.01" id="Slider" onchange="showSlider()"><label id="SliderText">0.5</label>
            <div id="Result"></div>
            {scripts}
            <p>­</p>
        </body>
    </html>"""
    file = open("page.html", "w")
    file.write(web)
    file.close()

if __name__ == "__main__":
  createPage()
