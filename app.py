from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hi car lease contract app'

if __name__ == "__main__":
    app.run()    