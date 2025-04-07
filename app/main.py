from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "KubeShop API is running"

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Casque Bluetooth", "price": 99},
        {"id": 2, "name": "Chargeur USB-C", "price": 19}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
