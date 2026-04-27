from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_csv("student_satisfaction.csv", sep="\t")
df.columns = df.columns.str.strip()

print("Columns:", df.columns.tolist())

@app.route("/")
def home():
    return "Campus Pulse API Running"

@app.route("/data")
def get_data():
    return jsonify(df.to_dict(orient="records"))

@app.route("/filter")
def filter_data():
    facility = request.args.get("facility")
    filtered = df[df["facility_rated"] == facility]
    return jsonify(filtered.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)