from backend import main
if __name__=="__main__":
    data={'mail':'abcdefg'}
def createOutputHTML(output:bool="", output_proba:float="",mots_spam:tuple=('',)) -> str:
    "crée le text: Spam/Ham + Raisons"
    if output == True:
        text=f"""<h2>🔴SPAM (Probabilité: {output_proba})</h2>
            <h3 id="reasons">Raisons:</h3>
            """
        for mot in mots_spam:
            text2+=f"<p>{mot}</p>"
    else: text = "🟢HAM"
    return text

"mail et sensibility viennent de l'HTML"
result = main.user_input(list(data['mail']))
html=createOutputHTML(result[0],result[1])
print(html)