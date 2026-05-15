from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load dataset

df = pd.read_csv("patient_data.csv")

# Clean stage names

df["Stages"] = df["Stages"].str.strip()

df["Stages"] = df["Stages"].replace({

    "HYPERTENSION (Stage-2).":
    "HYPERTENSION (Stage-2)",

    "HYPERTENSIVE CRISI":
    "HYPERTENSIVE CRISIS"

})

# Dashboard chart data

stage_counts = df["Stages"].value_counts()

labels = stage_counts.index.tolist()

values = stage_counts.values.tolist()

# Load trained model

model, label_encoders = pickle.load(
    open("hypertension_model.pkl", "rb")
)

# HOME PAGE

@app.route("/")
def home():

    return render_template("home.html")

# PREDICTION PAGE

@app.route("/predict")
def prediction_page():

    return render_template(
        "predict.html",
        labels=labels,
        values=values
    )

# PREDICTION RESULT

@app.route("/predict-result", methods=["POST"])
def predict():

    input_data = []

    for column, value in request.form.items():

        if column in label_encoders:

            encoded_value = label_encoders[column].transform([value])[0]

            input_data.append(encoded_value)

        else:

            input_data.append(value)

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    probability = model.predict_proba(input_array)

    confidence = round(max(probability[0]) * 100, 2)

    stage_name = label_encoders["Stages"].inverse_transform(
        prediction
    )[0]

    return render_template(

        "predict.html",

        prediction_text="Predicted Stage: " + stage_name,

        confidence=confidence,

        labels=labels,

        values=values

    )

# ABOUT PAGE

@app.route("/about")
def about():

    return render_template("about.html")

# CONTACT PAGE

@app.route("/contact")
def contact():

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)