import os
import mlflow

from flask import Flask, jsonify, request
import pandas as pd

os.environ['MLFLOW_TRACKING_URI'] = 'sqlite:///mlflow.db'
logged_model = 'runs:/56c4a92a15b845aa8c1f4b65490ca228/sk_models'
loaded_model = mlflow.sklearn.load_model(logged_model)
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming the input data is in JSON format
    prediction = loaded_model.predict(pd.DataFrame([data]))
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)