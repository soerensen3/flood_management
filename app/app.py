from flask import Flask
from flask import render_template

# from flask_cors import CORS, cross_origin

app = Flask(__name__)


# CORS(app)

@app.route("/")
def hello_world():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
