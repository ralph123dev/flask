from flask import Flask 

#initialisation de l'application Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>salut la team</h1>"

if __name__ == '__main__':
    app.run(debug=True)