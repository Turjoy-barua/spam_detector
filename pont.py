from flask import Flask, request, render_template
from backend import main
app = Flask(__name__,)

@app.route('/Spam', methods=['POST']) #trouvé dans Reddit
def server():
    if request.method == "POST":
        data=request.form.get("data")
        mail=request.form.get("mail")
        sensibility=request.form.get("sensibility")
        return data,sensibility
    return render_template('page.html')
def createOutputHTML(output:bool="", output_proba:float="",mots_spam:tuple=('',)) -> str:
    if output == True:
        text=f"""<h2>🔴SPAM (Probabilité: {output_proba})</h2>
            <h3 id="reasons">Raisons:</h3>
            """
        for mot in mots_spam:
            text2+=f"<p>{mot}</p>"
    else: text = "🟢HAM"
    return text
if __name__=='__main__': 
   app.run(host='localhost', port=5000)
print("a")

