
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Retail Sales Analysis & Future Sales Prediction")

st.write(
    "Interactive dashboard for historical retail sales analysis "
    "and future sales prediction."
)

# Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/valiotti/plotly-superstore/main/superstore.csv",
    sep=";"
)

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Total Orders", f"{total_orders:,}")

st.divider()

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly_sales["Order Date"],
    monthly_sales["Sales"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales Trend")
ax.grid(True)

st.pyplot(fig)

# Sales by Category
st.subheader("🏷️ Sales by Product Category")

category_sales = (
    df.groupby("Product Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)

# Future Sales Prediction
st.subheader("🔮 Future Sales Prediction")

future_sales = pd.read_csv("future_sales_predictions.csv")

future_sales["Month"] = pd.to_datetime(
    future_sales["Month"]
)

st.dataframe(
    future_sales,
    use_container_width=True
)

fig2, ax2 = plt.subplots(figsize=(12, 5))

ax2.plot(
    future_sales["Month"],
    future_sales["Predicted Sales"],
    marker="o"
)

ax2.set_xlabel("Month")
ax2.set_ylabel("Predicted Sales")
ax2.set_title("2013 Future Sales Forecast")
ax2.grid(True)

st.pyplot(fig2)

st.success("Dashboard loaded successfully! 🎉")
