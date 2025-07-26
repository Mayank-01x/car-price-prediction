from flask import Flask, render_template, request
import numpy as np
import os
import pickle

app = Flask(__name__)
model = pickle.load(open('trained_data_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    engine_size = request.form.get('engine-size')
    city_mpg = request.form.get('city-mpg')

    features = [float(engine_size), float(city_mpg)]
    final_input = np.array([features])
    prediction = model.predict(final_input)

    return render_template(
        'index.html',
        prediction_text=f"Predicted Car Price: ₹{prediction[0]:,.2f}",
        engine_size=engine_size,
        city_mpg=city_mpg
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

