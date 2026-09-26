# Vehicle Repeat Violation Prediction

This project predicts whether a vehicle is likely to be a repeat violator based on its traffic stop history.

## Project Overview
The system uses traffic violation data to analyze vehicle behavior patterns and classify vehicles as low-risk or high-risk. It follows a complete machine learning workflow, starting from raw data cleaning and feature engineering, through model training, and ending with a Streamlit-based prediction app.

## Problem Statement
Traffic violation records contain a large amount of stop-level information, but the goal is not to analyze individual stops alone. Instead, the project groups records by vehicle and identifies patterns that indicate repeated violation risk.

## Objectives
- Clean and preprocess raw traffic violation data
- Transform stop-level records into vehicle-level features
- Build a machine learning model for repeat-risk prediction
- Save the trained model
- Create a web app for predictions
- Export results to Excel for reporting

## Technologies Used
- Python
- pandas
- NumPy
- scikit-learn
- CatBoost
- Streamlit
- joblib
- openpyxl

## Project Structure

```text
mini projectnew2/
├── app.py
├── .gitignore
├── README.md
├── Data/
│   ├── Traffic_Violations.csv
│   ├── cleaned_stop_level_dataset.csv
│   ├── final_ml_dataset.csv
│   └── predicted_vehicle_risk.xlsx
├── model/
│   └── catboost_vehicle_repeat_violation_model.pkl
├── Notebook/
│   ├── cleaning.ipynb
│   ├── model_train.ipynb
│   └── catboost_info/
├── document/
│   ├── README.md
│   ├── methodology.md
│   ├── results.md
│   └── project_summary.md
└── visualization.pbix
```

## Data Workflow
1. Load the raw traffic violation dataset
2. Clean missing and inconsistent values
3. Normalize column names and formats
4. Create vehicle-level aggregate features
5. Define the repeat-risk target variable
6. Train the CatBoost classifier
7. Save the model for reuse
8. Run predictions in the Streamlit app
9. Export the output to Excel

## Model Details
The model is a binary classifier trained to predict:
- 0 = Low Risk
- 1 = High Risk

The model was trained using engineered vehicle features such as:
- accident count
- alcohol count
- fatal count
- property damage count
- average stop hour
- number of unique locations

## How to Run

### 1. Install dependencies
```bash
pip install pandas numpy scikit-learn catboost streamlit openpyxl joblib
```

### 2. Start the app
```bash
streamlit run app.py
```

### 3. Upload a CSV file
Upload either:
- a raw stop-level CSV, or
- a preprocessed vehicle-feature CSV

Then click the prediction button to generate results.

## Output
The application exports the prediction results to an Excel file stored in the Data folder.

## Project Outcome
This project demonstrates an end-to-end machine learning pipeline for real-world traffic risk prediction and provides a simple interface for users to make predictions without writing code.

## Notes
- The project is designed for vehicle-level repeat-risk analysis.
- The saved model file is reused by the app to avoid retraining every time.
- The project is suitable for portfolio, academic, or demonstration purposes.
