# Vehicle Repeat Violation Prediction Project

This project is a complete machine learning workflow for predicting whether a vehicle is likely to be involved in repeated traffic violations.

## Project Purpose
The goal of this project is to turn raw traffic stop records into useful risk insights. Instead of focusing on a single stop, the project studies behavior at the vehicle level to detect patterns that may indicate repeated risky conduct.

## What This Project Does
- Cleans raw traffic violation data
- Standardizes and organizes columns
- Creates vehicle-level summary features
- Trains a CatBoost classifier
- Saves the trained model
- Builds a Streamlit app for prediction
- Exports prediction results to Excel

## Folder Structure
- Data/: contains the datasets used in the project
- model/: contains the trained ML model
- Notebook/: contains the training and cleaning notebooks
- app.py: Streamlit web app
- document/: contains project documentation

## Core Workflow
1. Load traffic violation data
2. Clean and prepare the dataset
3. Convert stop-level data into vehicle-level features
4. Define repeat-risk labels
5. Train a binary classification model
6. Save the trained model
7. Use the model in a web app
8. Export results to Excel

## Main Technologies Used
- Python
- pandas
- NumPy
- scikit-learn
- CatBoost
- Streamlit
- openpyxl

## Result
The project produces a practical prediction system that can classify vehicles as low-risk or high-risk based on their historical violation patterns.
