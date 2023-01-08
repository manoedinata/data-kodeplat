from flask import Flask, jsonify
import json

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def get_data():
    with open("kode_plat.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    data = get_data()

    return jsonify(data)

@app.route("/<kode>")
def get_kode(kode):
    data = get_data()

    searched = next((item for item in data if item["kode"] == kode), None)
    if searched:
        return jsonify(searched)
    else:
        return jsonify({
            "error": "Kode tidak ditemukan!"
        })

if __name__ == "__main__":
    app.run()
