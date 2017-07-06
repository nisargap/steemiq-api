from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from calculate_grade import calculate_user
app = Flask(__name__)

cors = CORS(app)
@app.route("/grade/<username>")
def grade(username):
    return jsonify(calculate_user(username))

if __name__ == "__main__":
    app.run()
