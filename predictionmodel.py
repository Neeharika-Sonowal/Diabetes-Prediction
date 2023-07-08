from flask import Flask, render_template, request
from tensorflow import keras
from keras.models import load_model
from sklearn.preprocessing import StandardScaler
from pickle import load
scaler = load(open('scalar.pkl','rb'))
import numpy as np

# Load the saved model
model = keras.models.load_model('model.h5')
sc = StandardScaler()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
    # Get user input from the form
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        polyuria = int(request.form['polyuria'])
        polydipsia = int(request.form['polydipsia'])
        sudden_weight_loss = int(request.form['sudden_weight_loss'])
        weakness = int(request.form['weakness'])
        polyphagia = int(request.form['polyphagia'])
        genital_thrush = int(request.form['genital_thrush'])
        visual_blurring = int(request.form['visual_blurring'])
        itching = int(request.form['itching'])
        irritability = int(request.form['irritability'])
        delayed_healing = int(request.form['delayed_healing'])
        partial_paresis = int(request.form['partial_paresis'])
        muscle_stiffness = int(request.form['muscle_stiffness'])
        alopecia = int(request.form['alopecia'])
        obesity = int(request.form['obesity'])
        
    inputs = (age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,polyphagia,genital_thrush,visual_blurring,itching,irritability,
                   delayed_healing,partial_paresis,muscle_stiffness,alopecia,obesity)
   # Make a prediction using the loaded model
    ip_reshaped = np.asarray(inputs).reshape(1,-1)
    data = scaler.transform(ip_reshaped)
    print(data)
    prediction = model.predict(data)
    print(prediction)
    # Process the prediction result
    # Example: convert the prediction to a meaningful output
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)