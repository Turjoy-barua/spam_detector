from NotImplemented import *
def detect(mail,sensibility):
    result=NotImplemented
    html=createOutputHTML(NotImplemented,NotImplemented,NotImplemented)
    return

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

detect(mail="",sensibility="")