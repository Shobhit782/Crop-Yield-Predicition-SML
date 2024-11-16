from flask import Flask, request, render_template
import numpy as np
import pickle
import sklearn

print(sklearn.__version__)
app = Flask(__name__)

# Load your model and preprocessor
dtr = pickle.load(open('dtr.pkl', 'rb'))
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = request.form['Year']
        average_rain_fall_mm_per_year = request.form['average_rain_fall_mm_per_year']
        pesticides_tonnes = request.form['pesticides_tonnes']
        avg_temp = request.form['avg_temp']
        Area = request.form['Area']
        Item  = request.form['Item']

        # Prepare the features for prediction
        features = np.array([[Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp, Area, Item]], dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1, -1)

        # Convert prediction to a string for display
        predicted_yield = prediction[0][0] # Get the first element of the prediction array
        predicted_yield_str = f"{predicted_yield:.2f}"

        return render_template('index.html', prediction=predicted_yield_str)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
