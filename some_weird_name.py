from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route("/")
def main():
    with open("static/model.json") as json_file:
        json_model = json_file.read()
    return render_template("html_vis.html", model=str(json_model))

if __name__ == "__main__":
    app.run(debug=True)
