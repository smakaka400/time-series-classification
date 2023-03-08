from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("time_series_forest_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    """
    Flask app function to create an API at route /predict, returning the gender predictions given an input CSV.
    Loads a pre-trained model to create the predictions.
    Args:
        None
    Returns:
        A jsonified string of the predictions.
    """
    try:
        data = pd.read_csv(request.files['file'])
        predictions = model.predict(data).tolist()
        return jsonify({"predictions": predictions})
    except ZeroDivisionError:
        return jsonify("Error in CSV input data. Check file is of correct size and format.")
    except Exception:
        return jsonify("Error in input data. Check file is an input CSV of correct size and format.")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')