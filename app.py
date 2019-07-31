import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/defang/', methods=["GET", "POST"])
def defang(urls="https://twitter.com/comradeeevee"):
    urls = re.split('\r?\n?,', request.form['defang'])
    defanged = []
    for url in urls:
        defanged.append(url.replace("http", "hxxp").replace(".", "[.]").replace("/", "/\\").strip())
    return jsonify(defanged) 

@app.route('/refang/', methods=["GET", "POST"])
def refang(url="hxxps:/\/\\twitter.com/\comradeeevee"):
    urls = re.split('\r?\n?,', request.form['refang'])
    refanged = []
    for url in urls:
        refanged.append(url.replace("hxxp", "http").replace("[.]", ".").replace("/\\", "/").strip())
    return jsonify(refanged)

if __name__ == '__main__':
    app.run()