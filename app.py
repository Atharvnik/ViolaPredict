# STREAMLIT APP – VEHICLE REPEAT VIOLATION RISK

from pathlib import Path
import os
import subprocess

import joblib
import pandas as pd
import streamlit as st


# --------------------------------------------------
# APP CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Vehicle Repeat Violation Prediction",
    layout="wide",
)

st.title("🚦 Vehicle Repeat Violation Prediction System")
st.write(
    "Upload a vehicle-risk dataset or raw stop-level CSV → Click Predict → "
    "the prediction results are exported to Excel."
)


# --------------------------------------------------
# PATH SETTINGS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "catboost_vehicle_repeat_violation_model.pkl"
OUTPUT_PATH = BASE_DIR / "Data" / "predicted_vehicle_risk.xlsx"
EXPECTED_FEATURES = [
    "accident_count",
    "alcohol_count",
    "fatal_count",
    "property_damage_count",
    "avg_stop_hour",
    "unique_locations",
]
TARGET_COLUMN = "repeat_risk"


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = (
        cleaned.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
        .str.replace(r"/", "_", regex=True)
        .str.replace(r"-", "_", regex=True)
    )
    return cleaned


def build_vehicle_features(df: pd.DataFrame) -> pd.DataFrame:
    data = normalize_columns(df)
    required_raw_columns = {"make", "model", "year"}

    if not required_raw_columns.issubset(set(data.columns)):
        raise ValueError(
            "The uploaded CSV does not match the expected schema. "
            "Please upload either a model-ready vehicle dataset or a raw stop-level dataset."
        )

    data["vehicle_id"] = (
        data["make"].astype(str)
        + "_"
        + data["model"].astype(str)
        + "_"
        + data["year"].astype(str)
    )

    vehicle_df = data.groupby("vehicle_id").agg(
        total_violations=("vehicle_id", "count"),
        accident_count=("accident", lambda s: (s == "Yes").sum()),
        alcohol_count=("alcohol", lambda s: (s == "Yes").sum()),
        fatal_count=("fatal", lambda s: (s == "Yes").sum()),
        property_damage_count=("property_damage", lambda s: (s == "Yes").sum()),
        avg_stop_hour=("stop_hour", "mean"),
        unique_locations=("location", "nunique"),
    ).reset_index()

    return vehicle_df[EXPECTED_FEATURES]


def prepare_features_for_prediction(df: pd.DataFrame) -> pd.DataFrame:
    data = normalize_columns(df)

    if TARGET_COLUMN in data.columns:
        data = data.drop(columns=[TARGET_COLUMN])

    if set(EXPECTED_FEATURES).issubset(data.columns):
        return data[EXPECTED_FEATURES]

    if {"make", "model", "year"}.issubset(set(data.columns)):
        return build_vehicle_features(data)

    raise ValueError(
        "Missing required columns. Expected: "
        + ", ".join(EXPECTED_FEATURES)
        + " or raw stop-level columns including make, model, and year."
    )


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
    st.success("✅ ML Model Loaded Successfully")
except Exception as exc:
    st.error(f"❌ Model not found or could not be loaded: {exc}")
    st.stop()


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        feature_df = prepare_features_for_prediction(df)
    except Exception as exc:
        st.error(f"❌ Invalid dataset format: {exc}")
        st.stop()

    if st.button("🚀 Predict Risk"):
        with st.spinner("Predicting vehicle risk..."):
            predictions = model.predict(feature_df)
            probabilities = model.predict_proba(feature_df)[:, 1]

            output_df = feature_df.copy()
            output_df["predicted_risk"] = predictions
            output_df["risk_probability"] = probabilities
            output_df["predicted_risk_label"] = output_df["predicted_risk"].map(
                {0: "Low Risk", 1: "High Risk"}
            )

            OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
            with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
                output_df.to_excel(writer, sheet_name="Data", index=False)

            try:
                if os.name == "nt":
                    os.startfile(str(OUTPUT_PATH))
                else:
                    opener = "xdg-open" if os.system("which xdg-open > /dev/null 2>&1") == 0 else None
                    if opener:
                        subprocess.Popen([opener, str(OUTPUT_PATH)])
            except Exception:
                pass

        st.success("✅ Prediction Completed Successfully!")
        st.success("📊 Excel report created and opened automatically.")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")
st.caption(
    "Vehicle Pattern–Based Traffic Repeat Violation Prediction and Analysis"
)

