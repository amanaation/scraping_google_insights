from flask import Flask, render_template, request
from scrap_google_insights import Products

app = Flask(__name__)

@app.route("/post", methods=['GET'])
def process():
    sent_data = {}
    for key, value in request.args.items():
        sent_data[key] = str(value)
    prod = Products()
    prod.main(sent_data)
    return "<h1> <center> Scraped the Required Data</center></h1>"


if __name__ == "__main__":
    app.run(debug=True)
