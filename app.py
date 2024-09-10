from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

df=pd.read_csv("ml  linear regression project/deeep1.csv")

# Independent variables
terrain_dict = {
    'Desert': 10,
    'Forest': 15,
    'Mountain': 8,
}

weather_dict = {
    'Sunny': 0.5,
    'Cloudy': 0.7,
    'Rainy': 0.8,
    'Windy': 0.7,
}
#
# Perform linear regression
# calculated slope using y=mx+c formula
slope = 1.5  # slope = (n * sum(xy) - sum(x) * sum(y)) / (n * sum(x**2) - sum(x) ** 2)
# calculated intercept by using y`=mx`+c formula here
intercept = 75  # intercept = (sum(y) - slope * sum(x)) / n

# Defing a function to predict the Roadrunner's speed
def predict_roadrunner_speed(terrain, weather):
    terrain_difficulty = terrain_dict.get(terrain, 0)
    weather_condition = weather_dict.get(weather, 0)
    return slope * terrain_difficulty + slope * weather_condition + intercept

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_speed = None
    if request.method == "POST":
        terrain = request.form["terrain"]
        weather = request.form["weather"]
        predicted_speed = predict_roadrunner_speed(terrain, weather)
    return render_template("index.html", predicted_speed=predicted_speed)

@app.route("/predict_api", methods=["POST"])
def predict_api():
    try:
        input_data = request.get_json()
        terrain = input_data.get("terrain")
        weather = input_data.get("weather")
        predicted_speed = predict_roadrunner_speed(terrain, weather)
        response = {"predicted_speed": predicted_speed}
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
