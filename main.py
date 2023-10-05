from flask import Flask, request , jsonify,render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/h',methods=["POST"])
def predict():
    data=request.get_json()
    response = {"answer":data["data"]}
    return jsonify(response)
if __name__ == "__main__":
    app.run(debug=True)