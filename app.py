import requests
from flask import Flask, request, render_template
from diet_model import DietConsultant

app = Flask(__name__, template_folder="templates", static_folder="static")

def is_connected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        name = request.form["name"]
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        goal = request.form["goal"]
        preference = request.form.get("preference", "general")
        disease = request.form.get("disease", None)

        consultant = DietConsultant(name, age, weight, height, goal, preference, disease)
        diet_plan = consultant.suggest_diet()

        return render_template("result.html", name=name, diet_plan=diet_plan)
    except Exception as e:
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    if is_connected():
        print("Internet connection detected. Running the application...")
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("No internet connection. Please connect to the internet and restart the application.")
