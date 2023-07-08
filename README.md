# Diabetes-Prediction
This repository provides a comparison of different diabetes prediction models. The purpose of this project is to evaluate the performance of various machine learning algorithms for predicting diabetes in patients. The models are trained on a dataset consisting of various features related to patients' medical history and lifestyle.
## Dataset 

Features
- Age: The age of the individual in years.
- Gender: The gender of the individual, typically categorized as male or female.
- Polyuria: Excessive urination.
- Polydipsia: Excessive thirst.
- Sudden weight loss: Rapid and unintentional weight loss experienced by the individual.
- Weakness: Generalized lack of strength or energy.
- Polyphagia: Increased hunger or excessive appetite.
- Genital thrush: Presence of a fungal infection in the genital area.
- Visual blurring: Blurred vision or difficulty focusing.
- Itching: Persistent itching or skin irritations.
- Irritability: Frequent mood swings or easily becoming annoyed.
- Delayed healing: Slow healing of wounds or injuries.
- Partial paresis: Partial paralysis or weakness in certain body parts.
- Muscle stiffness: Stiffness or difficulty in moving muscles.
- Alopecia: Hair loss or baldness.
- Obesity: Excessive body weight or high body mass index (BMI).
- Class: The target variable indicating whether an individual has diabetes or does not have diabetes.
## Models

The following models have been implemented and evaluated for diabetes prediction:

1. Logistic Regression
2. Naive Bayes
3. Decision Tree
4. Random Forest
5. Artificial Neural Network

Each model is trained on the dataset and evaluated using various performance metrics such as accuracy, precision, recall, and F1-score. The models are compared based on these metrics to assess their predictive capabilities for diabetes.

## Results

The results of the comparison are presented in the notebook, including performance metrics and visualizations. The comparison aims to provide insights into the strengths and weaknesses of each model for diabetes prediction.

The best model is saved in `model.h5`.

## Flask Web App

In addition to the model comparison, this repository provides a Flask web application for diabetes prediction. The web app allows users to input their medical information and get a prediction for the likelihood of having diabetes. The prediction is made using the selected machine learning model.

To run the Flask web app locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the `predictionmodel.py` file using the command `python predictionmodel.py`.
4. Access the web app in your browser at `http://localhost:5000`.

## Contact

For any questions or inquiries, please contact [neeharika26sonowal@gmail.com](mailto:neeharika26sonowal@gmail.com).