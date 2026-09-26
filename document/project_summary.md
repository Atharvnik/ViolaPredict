# Vehicle Repeat Violation Prediction Project

## Overview
This project was built to help predict whether a vehicle is likely to be involved in repeat traffic violations. Instead of looking at single stops only, the project groups traffic stops by vehicle and studies the overall pattern of that vehicle over time. The idea is to identify risky vehicles early and support better monitoring and decision-making.

## Project Goal
The main goal was to create an end-to-end machine learning project that could:
- collect and clean traffic stop data,
- convert raw stop records into vehicle-level features,
- train a model to predict repeat-risk vehicles,
- save the trained model,
- and provide a simple web app where a user can upload a dataset and get predictions.

## Step 1: Data Collection
The project uses traffic violation data stored in the Data folder. The raw dataset contains many stop-level records, including information such as:
- date and time of stop,
- vehicle make and model,
- accident or alcohol flags,
- property damage,
- fatality data,
- location and state,
- and other stop-related details.

This raw data is rich, but it is not directly ready for machine learning because each row represents one traffic stop rather than one vehicle.

## Step 2: Data Cleaning
The first major step was cleaning the dataset. This included:
- removing duplicate rows,
- fixing column names and standardizing them,
- filling missing values,
- converting date and time fields into useful formats,
- creating new time-based features like stop hour, day, month, and weekday,
- and keeping only the relevant columns needed for modeling.

The cleaned dataset was saved as a processed file so that it could be reused for future analysis and model building.

## Step 3: Feature Engineering
The project then moved from stop-level data to vehicle-level data.

Instead of predicting risk for a single stop, the project grouped records by each vehicle. A vehicle was identified using a combination of:
- make,
- model,
- and year.

For each vehicle, the project created summary features such as:
- total number of violations,
- accident count,
- alcohol count,
- fatal count,
- property_damage count,
- average stop hour,
- and number of unique locations visited.

These features are much more useful for identifying a vehicle that repeatedly shows risky behavior.

## Step 4: Target Definition
The target variable, called repeat_risk, was defined based on how frequently a vehicle appeared in the stop data.

Vehicles with unusually high numbers of violations were labeled as high risk, while others were labeled as low risk. This made the problem a binary classification task:
- 0 = Low Risk
- 1 = High Risk

This step is essential because the model learns from these labels to classify future vehicles.

## Step 5: Model Training
The project used CatBoost, a powerful machine learning algorithm for tabular data. CatBoost was chosen because it handles structured datasets well and works effectively with classification problems.

The data was split into training and testing sets, and the model was trained using the engineered vehicle features. The training process included:
- setting model hyperparameters,
- using class weighting to handle imbalance,
- and evaluating classification performance.

The model was then tested using metrics such as:
- accuracy,
- classification report,
- and ROC-AUC score.

This helped confirm whether the model could distinguish between low-risk and high-risk vehicles in a meaningful way.

## Step 6: Model Saving
After the model performed well, it was saved to the model folder using joblib. This makes the model reusable later in the app without retraining every time.

The saved model file is used as the core prediction engine in the final project application.

## Step 7: Streamlit App Development
A web application was built using Streamlit so that end users do not need to write code or run notebooks manually.

The app allows a user to:
- upload a CSV file,
- either provide vehicle-ready features or raw stop-level data,
- run the model prediction,
- and receive the predicted risk output.

The app also prepares the uploaded dataset if it is in raw format by converting it into the same feature structure used during training.

## Step 8: Prediction Output
After prediction, the app creates an Excel file with the prediction results. The output includes:
- the original feature values,
- the predicted risk label,
- the probability score,
- and a human-readable label such as Low Risk or High Risk.

This makes the output suitable for reporting, sharing, and further analysis in Excel.

## Step 9: Final Outcome
The project successfully creates a complete machine learning workflow that:
- reads real-world traffic violation data,
- prepares the data for modeling,
- trains a CatBoost classifier,
- saves the model,
- and exposes it through a simple interactive interface.

This means the project is not just a notebook experiment; it is a usable prediction system with a practical purpose.

## Key Learning Points
This project demonstrates a real-world ML pipeline:
- data understanding,
- cleaning,
- feature engineering,
- supervised learning,
- model evaluation,
- deployment in a lightweight app,
- and export of results to business-friendly formats.

It also shows how raw operational data can be transformed into insight and used for decision-making.

## Project Value
This project is useful because it solves a realistic problem in traffic enforcement and vehicle monitoring. It can help identify vehicles that repeatedly show risky behavior, which is valuable for:
- traffic monitoring,
- enforcement planning,
- risk analysis,
- and operational decision support.

## Conclusion
The project is a complete end-to-end data science and machine learning solution. It starts with messy real-world traffic data, cleans and transforms it, trains a predictive model, and delivers predictions through an easy-to-use application. In simple terms, the project turns raw traffic data into actionable risk information for repeat-violation prediction.
