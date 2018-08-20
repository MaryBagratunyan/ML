from flask import Flask, request
import pickle
import pandas as pd
import os

model = pickle.load(open( "model.pkl", "rb" ))
app = Flask(__name__)

@app.route('/')
def greeting():
    return"""
        <h1> Type the following link </h1>
        <h2> /predict?full_sq=40&life_sq=40.0&area_m=21494094.8&build_year=2015 </h2>
        """

@app.route('/predict')
def predict():
    full_sq = request.args.get('full_sq')
    life_sq = request.args.get('life_sq')
    area_m = request.args.get('area_m')
    build_year = request.args.get('build_year')

    result = model.predict([[full_sq, life_sq, area_m, build_year]])
    return '<h1> The price is {} <h1>'.format(result[0])

if __name__ == "__main__":
    port = int(os.environ["PORT"])
    app.run(host='0.0.0.0', port=port)