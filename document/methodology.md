# Methodology

## 1. Data Collection
The project starts with a traffic violation dataset containing many records of individual stops. Each record includes vehicle information, stop details, and violation-related fields.

## 2. Data Cleaning
The raw data was cleaned to improve quality and consistency. This step involved:
- removing duplicate records,
- fixing column names,
- filling missing values,
- converting date and time values into usable formats,
- and preparing the dataset for feature engineering.

## 3. Feature Engineering
The dataset was transformed from stop-level records into vehicle-level features. This was done by grouping the data by vehicle using the vehicle’s make, model, and year.

Key engineered features include:
- accident_count
- alcohol_count
- fatal_count
- property_damage_count
- avg_stop_hour
- unique_locations

These features capture the overall risk behavior of a vehicle rather than just one isolated stop.

## 4. Target Variable Definition
The target variable was defined as repeat_risk. Vehicles with a high number of violations were labeled as high risk, while the rest were labeled as low risk.

This created a binary classification problem:
- 0 = Low Risk
- 1 = High Risk

## 5. Model Selection
CatBoost was selected because it performs well on structured tabular data and is suitable for classification tasks.

The model was trained using the engineered vehicle features and evaluated with common metrics such as:
- accuracy,
- classification report,
- and ROC-AUC score.

## 6. Model Saving
Once training was complete, the model was saved as a pickle file in the model folder. This allows the project to reuse the trained model without retraining it for every prediction.

## 7. Deployment in Streamlit
A Streamlit app was created so users can upload CSV data and receive prediction results quickly and easily. The app also handles the case where raw stop-level data is uploaded by translating it into model-ready features.

## 8. Exporting Results
The app writes the prediction output to an Excel file. This makes the results easy to view, share, and analyze in a familiar business format.

## Summary
The methodology follows a standard machine learning pipeline: collect data, clean it, engineer meaningful features, train a model, validate it, and deploy it in an easy-to-use interface.
