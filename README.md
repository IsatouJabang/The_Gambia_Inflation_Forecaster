# 🇬🇲 The Gambia: Food Inflation ML Forecasting Dashboard

An interactive machine learning platform built to predict short-term consumer food price horizons in The Gambia using optimized gradient-boosted trees (**XGBoost**). 

This application allows policymakers, researchers, and analysts to simulate real-time macroeconomic shifts (such as exchange rate shocks or policy rate adjustments) and instantly view 1-month-ahead predictive variations against 24 months of historical tracking context.

---

## Project Structure

This repository is organized into the following clear workspace modules:
* `data/` : Contains the processed macroeconomic baseline dataset.
* `models/` : Holds the serialized, trained XGBoost core regression models.
* `src/` : Application engine containing the Streamlit frontend user interface.

---

## Key Features

* **Live Inference Engine:** Instantly recalculates food inflation predictions using sliding macroeconomic parameters.
* **Macroeconomic Feature Pipeline:** Models complex core relationships including lag effects (`Inflation_Lag1`, `Exchange_Change_Lag1`), Treasury Bill yields, and Central Bank interventions.
* **Interactive Visualization:** Leverages dynamic Plotly timelines to render historical baseline trends side-by-side with dynamic AI marker projections.

---

## Local Installation & Setup

Follow these quick commands to spin up this environment locally on your machine:

### Clone the repository and enter the directory
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/The-Gambia-Inflation-Forecaster.git](https://github.com/YOUR_GITHUB_USERNAME/The-Gambia-Inflation-Forecaster.git)
cd The-Gambia-Inflation-Forecaster

### Launch the Streamlit server dashboard
```bash
streamlit run app.py
