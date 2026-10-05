# Retail Sales Analysis & Future Sales Prediction

## 📌 Project Overview

This project analyzes historical retail sales data and uses Machine Learning to predict future sales.

The project includes:
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Feature engineering
- Sales prediction using Random Forest
- Monthly time-series forecasting
- Future sales prediction
- Interactive Streamlit dashboard

## 🎯 Objectives

- Understand retail sales patterns
- Analyze sales and profit by category and region
- Identify important sales trends
- Build a Machine Learning model for sales prediction
- Forecast future monthly sales
- Present results through an interactive dashboard

## 📊 Dataset

The project uses a Superstore retail sales dataset containing information about:

- Order Date
- Sales
- Profit
- Order Quantity
- Discount
- Product Category
- Product Sub-Category
- Region
- Customer Segment
- Shipping information

The dataset contains 8,394 records and 21 original columns.

## 🔍 Exploratory Data Analysis

Key findings:

- **Technology** has the highest total sales among product categories.
- **Technology** also has the highest total profit.
- **West** has the highest total sales among regions.
- **Ontario** has the highest total profit among regions.
- Sales and profit have a moderate positive correlation.
- December has the highest total sales among months in the dataset.

## 🤖 Machine Learning

### Order-Level Sales Prediction

A Random Forest Regressor was used to estimate sales using order-related features.

**Results:**

| Metric | Score |
|---|---:|
| MAE | 131.85 |
| RMSE | 519.99 |
| R² Score | 0.9758 |

This model estimates sales for individual orders based on available order-level features.

### Future Sales Forecasting

Monthly sales data was created and lag-based features were generated:

- Previous month sales
- 3-month lag
- 12-month lag
- 3-month rolling average
- Month
- Quarter

An improved Random Forest forecasting model achieved:

| Metric | Score |
|---|---:|
| MAE | 38,567.59 |
| RMSE | 51,370.17 |
| R² Score | -0.1778 |

The forecasting model is treated as a baseline/experimental model because the test-set R² is still negative.

## 🔮 Future Sales Predictions

The model generated predictions for January–June 2013:

| Month | Predicted Sales |
|---|---:|
| January 2013 | 285,863.18 |
| February 2013 | 290,397.62 |
| March 2013 | 282,612.00 |
| April 2013 | 288,964.33 |
| May 2013 | 264,516.34 |
| June 2013 | 257,104.96 |

## 📈 Streamlit Dashboard

The project includes an interactive Streamlit dashboard showing:

- Total sales
- Total profit
- Total orders
- Monthly sales trend
- Sales by product category
- Future sales predictions

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Random Forest
- Streamlit
- Google Colab
- GitHub

## 📁 Project Structure

```text
retail-sales-forecasting-ml/
│
├── README.md
├── app.py
└── future_sales_predictions.csv
