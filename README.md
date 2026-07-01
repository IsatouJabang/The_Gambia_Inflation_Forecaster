🇬🇲 The Gambia: Food Price Prediction Dashboard

This is a smart web tool that predicts where food prices are heading in The Gambia. It uses artificial intelligence (AI) to let users test out different economic situations and instantly see how they might change the cost of food.

[Click here to view the live dashboard](https://the-gambia-inflation-forecaster.streamlit.app/)**


Why This Matters
When the price of everyday items like rice, oil, and vegetables goes up, it directly affects how much food a family can afford. Traditional economic reports only look at what *already* happened in the past. This project builds a forward-looking tool so that policymakers, researchers, and everyday citizens can anticipate price changes before they happen.


How the AI Works (In Simple Terms)
Instead of just guessing, we taught a computer model to find patterns by looking at past historical data from The Gambia and Countries that's economic activities might afftect the Gambia such as: China, Senegal, Russia, Netherlands, Ukraine, USA and UK. 

The AI looks at how food prices react when things like this change:
Overall Inflation: How fast general prices are rising across the country.
Exchange Rates How strong the Gambian Dalasi is performing against foreign currencies.
Interest Rates The rules set by the Central Bank and Treasury bills that control how money flows through the economy.

We used the optimized gradient-boosted trees (XGBoost), a highly accurate machine learning algorithm.
Think of it like an incredibly smart calculator that looks at the past few months of data, connects the dots, and predicts next month's food price trends.

Project Structure
This repository is organized cleanly so anyone can find files easily:

![Project Folder Structure](structure)

Key Features

Complete ML Lifecycle Transparency: Full tracking from raw data ingestion and structural transformations to fully validated predictive states.

Live Inference Engine: Instantly recalculates food inflation predictions using sliding macroeconomic parameters within the dashboard interface.

Scenario Simulation Workspace: Allows policymakers and analysts to test hypothetical exchange rate shocks or policy rate adjustments and instantly view 1-month-ahead predictive 
variations against historical benchmarks.

Interactive Visualization: Leverages dynamic Plotly timelines to render historical baseline trends side-by-side with live model marker projections.

Evaluation Feature Matrix: The underlying forecasting model evaluates the following core macroeconomic indicators and historical feedback metrics to generate its predictions:

Feature Name: 
Inflation
Inflation_Lag1
Food_Inflation
Exchange_Change
Exchange_Change_Lag1
Policy_Rate
TBill_91D		

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

