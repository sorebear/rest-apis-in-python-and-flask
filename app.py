from flask import Flask

app = Flask(__name__)

@app.route('/') #http://www.google.com/
def home():
    return "Hello, world!"

@app.route('/mcdonalds')
def mcdonalds():
    return "Can I get a McPick Two!?"

app.run(port=5000)
