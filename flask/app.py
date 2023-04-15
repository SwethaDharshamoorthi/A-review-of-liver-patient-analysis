import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from flask_ngrok import run_with_ngrok
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)
run_with_ngrok(app)

model1= pickle.load(open('ETC.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['GET', "POST"])
def predict():
    input_values = [float(x) for x in request.form.values()]
    inp_features = [input_values]
    print(inp_features )
    prediction = model1.predict(inp_features)
    if prediction == 1:
        return render_template('index.html', prediction_text=('You have a liver disease,Please consult a doctor')
    else:
        return render_template('index.html', prediction_text=('You don't have liver disease'))


app.run()
