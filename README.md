
# 🚗 Car Price Prediction Web App

This is a Machine Learning-powered web application that predicts car prices based on features like **engine size** and **city mileage**. Built with **Python**, **Flask**, and a pre-trained regression model.

[![Render](https://img.shields.io/badge/Deployed%20on-Render-00c7b7?logo=render&logoColor=white)](https://car-price-prediction-830k.onrender.com)

---

## 📦 Project Structure

```
Car-Price-Prediction/
├── app.py                   # Flask web app
├── automobile_data.csv      # Training dataset
├── trained_data_model.pkl   # Saved ML model (Pickle format)
├── train_model.ipynb        # Jupyter notebook for training the model
├── templates/
│   └── index.html           # Web form for user input
```

---

## 🚀 Features

- Predict car price using engine size and mileage
- Simple & responsive HTML interface
- Fast predictions using a trained model
- Easy to deploy or run locally

---

## 🧠 Model Details

- Trained using `scikit-learn`
- Regression model (`LinearRegression` or similar)
- Input features:
  - `engine-size` (cc)
  - `city-mpg` (Miles Per Gallon)

---

## 🛠️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Mayank-01x/car-price-prediction.git
cd car-price-prediction
```

### 2. Install Dependencies
Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:

```bash
pip install flask pandas numpy scikit-learn
```

### 3. Run the App

```bash
python app.py
```

Then open your browser at:  
🔗 http://127.0.0.1:5000

---

## 🌐 Live Demo (Optional)

> _You can deploy this on platforms like_:
- Render (recommended)
- Replit
- Hugging Face Spaces

Want help deploying? Ping me!

---

## 🧑‍💻 Author

**Mayank Aggarwal**  
GitHub: [@Mayank-01x](https://github.com/Mayank-01x)

---

## 📜 License

MIT License – feel free to use and adapt!
