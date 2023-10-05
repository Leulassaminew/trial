from flask import Flask, request , jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "home"

@app.route('/h',methods=["POST"])
def predict():
    data=request.get_json()
    response = {"answer":data["data"]}
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)
