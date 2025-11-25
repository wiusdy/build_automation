from flask import Flask, render_template

app = Flask(__name__, template_folder="../web")

@app.route("/")
def home():
    message = "Hello CI/CD Pipeline! This is a mock AWS deployment."
    return render_template("index.html", message=message)
