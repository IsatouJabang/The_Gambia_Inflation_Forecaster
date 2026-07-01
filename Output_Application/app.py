import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="The Gambia Inflation Forecaster", layout="wide")
st.title("🇬🇲 The Gambia: Food Inflation ML Forecasting Dashboard")
st.write("An interactive AI platform predicting short-term food price horizons using optimized XGBoost models.")

# 2. LOAD BACKEND RESOURCES
# Find the directory that app.py is sitting in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
@st.cache_resource 
def load_resources():
    df = pd.read_csv("Processed_Data_ML.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    model_month = joblib.load("xgboost_model_m1.pkl") 
    return df, model_month
    csv_path = os.path.join(BASE_DIR, "Processed_Data_ML.csv")

df, model_month = load_resources()

# 3. SIDEBAR INTERACTIVE INPUT CONTROLS
st.sidebar.header("Current Economic Scenario Inputs")
st.sidebar.write("Adjust these sliders to simulate real-time macroeconomic changes:")

input_inflation = st.sidebar.slider("Current YoY Aggregate Inflation (%)", 0.0, 30.0, float(df['Inflation'].iloc[-1]))
input_food = st.sidebar.slider("Current YoY Food Inflation (%)", 0.0, 40.0, float(df['Food_Inflation'].iloc[-1]))
input_fx = st.sidebar.slider("Month-over-Month Exchange Rate Change (%)", -10.0, 10.0, 0.0)
input_policy = st.sidebar.slider("Central Bank Policy Rate (%)", 0.0, 25.0, float(df['Policy_Rate'].iloc[-1]))
input_tbills = st.sidebar.slider("91-Day Treasury Bill Yield (%)", 0.0, 25.0, float(df['TBill_91D'].iloc[-1]))

# Create lookback feature values lookups
input_fx_lag1 = float(df['Exchange_Change'].iloc[-2]) if 'Exchange_Change' in df.columns else 0.0
inflation_lag1 = float(df['Inflation'].iloc[-1]) 

# 4. LIVE INFERENCE ENGINE
current_features = pd.DataFrame([{
    'Inflation': input_inflation,
    'Inflation_Lag1': inflation_lag1,
    'Food_Inflation': input_food, 
    'Exchange_Change': input_fx,
    'Exchange_Change_Lag1': input_fx_lag1,
    'Policy_Rate': input_policy,
    'TBill_91D': input_tbills
}])

# Enforce layout configuration order required by XGBoost
expected_order = ['Inflation', 'Inflation_Lag1', 'Food_Inflation', 'Exchange_Change', 'Exchange_Change_Lag1', 'Policy_Rate', 'TBill_91D']
current_features = current_features[expected_order]

# Calculate live dynamic prediction
predicted_m1 = model_month.predict(current_features)[0]

# 5. RENDER THE INTERACTIVE GRAPH
st.subheader("Interactive 1-Month Ahead Predictive Analysis")

col1, col2 = st.columns([1, 3])

with col1:
    st.metric(label="Current Food Inflation State", value=f"{input_food:.2f}%")
    st.metric(label="AI Forecasted Month 1 Inflation", value=f"{predicted_m1:.2f}%", 
              delta=f"{predicted_m1 - input_food:.2f}% indicating shift")

with col2:
    fig = go.Figure()
    
    # Historical data plot line
    fig.add_trace(go.Scatter(x=df['Date'].tail(24), y=df['Target_Food_Inflation_Month1'].tail(24),
                             name="Historical Record", line=dict(color='black', width=2)))
    
    # Appended forecast point
    future_date = df['Date'].iloc[-1] + pd.DateOffset(months=1)
    fig.add_trace(go.Scatter(x=[future_date], y=[predicted_m1],
                             name="XGBoost Live Forecast", mode="markers",
                             marker=dict(color='crimson', size=12, symbol='x')))
    
    fig.update_layout(title="Consumer Food Inflation Timeline Matrix",
                      xaxis_title="Timeline", yaxis_title="YoY Inflation Percentage (%)",
                      template="plotly_white")
    
    st.plotly_chart(fig, width='stretch')
