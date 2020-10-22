from flask import Flask, render_template, request
from scrap_google_insights import Articles

app = Flask(__name__)


@app.route("/get", methods=['POST', 'GET'])
def home():
    return render_template("index.html")


@app.route("/post", methods=['GET'])
def process():
    sent_data = {}
    for key, value in request.args.items():
        sent_data[key] = str(value)
    art = Articles()
    art.main(sent_data)
    return "<h1> <center> Scraped the Required Data</center></h1>"


if __name__ == "__main__":
    app.run(debug=True)
