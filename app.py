from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "¡Hola, App Runner desde Flask!"})

@app.route("/api/suma")
def suma():
    a, b = 5, 3
    return jsonify({"resultado": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
