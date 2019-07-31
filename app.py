from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/defang/', methods=["GET", "POST"])
def defang(url="https://twitter.com/comradeeevee"):
    url = request.form['defang']
    defanged = url.replace("https", "hxxps").replace(".", "[.]").replace("/", "/\\")
    return f'defanged: {defanged}' 

@app.route('/refang/', methods=["GET", "POST"])
def refang(url="hxxps:/\/\\twitter.com/\comradeeevee"):
    url = request.form['refang']
    refanged = url.replace("hxxps", "https").replace("[.]", ".").replace("/\\", "/")
    return f'refanged: {refanged}'

if __name__ == '__main__':
    app.run()