# Results and Findings

## Model Purpose
The project successfully built a predictive model to estimate whether a vehicle is at risk of repeat violations based on historical traffic stop patterns.

## Key Outcome
The trained CatBoost model was able to produce valid predictions from the project’s vehicle-level features and from raw stop-level data when converted to the correct input format.

## Important Observations
- The model works best when the input matches the feature structure used during training.
- Raw stop-level data must be aggregated into vehicle-level statistics before prediction.
- The final app supports both feature-ready datasets and raw traffic stop files.

## Evaluation
The model was evaluated using:
- accuracy,
- classification report,
- and ROC-AUC score.

These metrics help confirm whether the model can distinguish between vehicles with low and high repeat-risk patterns.

## Practical Interpretation
The project demonstrates that historical traffic data can be converted into meaningful risk signals. Vehicles with repeated violations, accidents, alcohol-related flags, or high stop frequency are more likely to be categorized as high-risk vehicles.

## Business Value
This project has usefulness in:
- traffic monitoring,
- enforcement planning,
- identifying recurring risky vehicles,
- and supporting analytical reporting.

## Final Result
The final system is a working end-to-end project that combines data cleaning, feature engineering, machine learning, and a user-friendly prediction interface.

The project is not only a model training exercise; it is a practical risk prediction system that can be reused and extended.
