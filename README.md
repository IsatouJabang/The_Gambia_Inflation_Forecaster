# 🇬🇲 The Gambia: Food Inflation ML Forecasting Dashboard

An interactive, end-to-end machine learning platform built to predict short-term consumer food price horizons in The Gambia using optimized gradient-boosted trees (**XGBoost**). 

This repository documents the full academic data science lifecycle—spanning raw macroeconomic ingestion, lag-structural feature engineering pipelines, hyperparameter evaluation architectures, and production dashboard deployment.

---

## Project Structure

The workspace is organized to mirror an industry-standard machine learning development pipeline:

AI_Project/
├── Data/                      
├── PreProcessing/             
├── Modeling/                   
├── Documentation/             
├── Output_Application/         
│   ├── app.py                  
│   ├── Processed_Data_ML.csv   
│   ├── xgboost_model_m1.pkl    
│   └── Dashboard.ipynb          
├── .gitignore                  
├── requirements.txt           
└── README.md                   

Key Features

Complete ML Lifecycle Transparency: Full tracking from raw data ingestion and structural transformations to fully validated predictive states.

Live Inference Engine: Instantly recalculates food inflation predictions using sliding macroeconomic parameters within the dashboard interface.

Scenario Simulation Workspace: Allows policymakers and analysts to test hypothetical exchange rate shocks or policy rate adjustments and instantly view 1-month-ahead predictive 
variations against historical benchmarks.

Interactive Visualization: Leverages dynamic Plotly timelines to render historical baseline trends side-by-side with live model marker projections.

Evaluation Feature Matrix
The underlying forecasting model evaluates the following core macroeconomic indicators and historical feedback metrics to generate its predictions:

Feature Name: 
Inflation
Inflation_Lag1
Food_Inflation
Exchange_Change
Exchange_Change_Lag1
Policy_Rate
TBill_91D		

Data Type:
Continuous
Continuous
Continuous
Continuous
Continuous
Continuous
Continuous

Operational Description:			
Current Year-over-Year (YoY) Aggregate Inflation Rate (%)				
Historical baseline consumer aggregate index offset (Month -1)				
Anchor baseline Year-over-Year food category performance metric				
Month-over-Month value tracking shifts in local currency pairings				
Delayed structural transmission shocks from exchange adjustments				
Central Bank of The Gambia standard baseline benchmark interest rate				
Short-term government debt instruments yield marker index	

Model Architecture & Deserialization
The core forecasting model was built using the XGBoost Regressor framework, utilizing optimized gradient-boosted tree ensembles capable of mapping complex structural non-linearities inherent in developing financial markets. Model weights and training configurations are saved and deserialized instantly on execution via memory-mapped joblib streams.

Local Installation & Setup

Follow these quick commands to spin up and run the entire workspace stack locally on your computer:
1. Clone the repository and enter the directory
   Bash
git clone [https://github.com/IsatouJabang/The_Gambia_Inflation_Forecaster.git](https://github.com/IsatouJabang/The_Gambia_Inflation_Forecaster.git)
cd The_Gambia_Inflation_Forecaster

2. Install required application libraries
Bash
pip install -r requirements.txt --only-binary :all:

3. Launch the deployment dashboard server
streamlit run Output_Application/app.py

