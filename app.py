from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/defang/', methods=["GET", "POST"])
def defang(url="https://twitter.com/comradeeevee"):
    defanged = url.replace("https", "hxxps").replace(".", "[.]").replace("/", "/\\")
    return f'defanged: {defanged}' 

@app.route('/refang/', methods=["GET", "POST"])
def refang(url="hxxps:/\/\\twitter[.]com/\comradeeevee"):
    refanged = url.replace("hxxps", "https").replace("[.]", ".").replace("/\\", "/")
    return f'refanged: {refanged}'

if __name__ == '__main__':
    app.run()