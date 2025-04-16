from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the pre-trained model and scaler
model = pickle.load(open('random_forest_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route("/", methods=["GET"])
def home_redirect():
    return render_template("home.html")

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/start", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return predict()
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form

    # Mappings for categorical values
    painkiller_map = {
        'Never Used': 1, 'Over a Year Ago': 2,
        'Past Year': 3, 'Past Month': 4
    }

    yes_no_map = {'Yes': 1, 'No': 0, 'Not Sure': 2}
    health_map = {'Very Good': 4, 'Good': 3, 'Excellent': 2, 'Fair': 1, 'Poor': 0}
    education_map = {
        'Less than High School': 1,
        'High School Graduate': 2,
        'College Graduate': 3,
        'Postgraduate / Advanced Degree': 4,
        'Some College or Associate Degree': 0
    }
    gender_map = {'female': 0, 'male': 1}

    try:
        features = [
            painkiller_map.get(data['Painkiller_Use_Recency'], 0),
            yes_no_map.get(data['Mental_Health_Think'], 0),
            yes_no_map.get(data['Dependent_On_Prescription_Pills'], 0),
            float(data['Age_Group']),
            education_map.get(data['Education_Highest_Category'], 0),
            yes_no_map.get(data['Pain_Relievers_Non_Medical_Lifetime_Use'], 0),
            health_map.get(data['health.1'], 0),
            gender_map.get(data['Gender'].lower(), 0),
            yes_no_map.get(data['Currently_Using_Drugs'], 0),
            float(data['total_drug_use_days'])
        ]

        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]

        if prediction == 1:
            risk_level = "High Risk"
            recommendation = (
                "It appears you're at high risk of drug use. "
                "We strongly recommend seeking professional support as soon as possible. "
                "It's important to address this issue with healthcare providers to prevent further harm. "
                "Consider therapy, counseling, and staying connected with your support system."
            )
        else:
            risk_level = "Low Risk"
            recommendation = (
                "You are at low risk of drug use. We strongly encourage you to stay completely away from any kind of drug use in the future. "
                "Maintaining a healthy lifestyle and staying mentally strong are important. "
                "Never start using drugs — even a small trial can lead to serious problems. "
                "If you ever feel stressed or tempted, seek support from family, friends, or a healthcare professional."
            )

        return render_template("result.html", risk_level=risk_level, recommendation=recommendation)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
