import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Load the dataset
    data = pd.read_csv("Walmart_sales_cleaned.csv")  

    # Sidebar options
    analysis_option = st.sidebar.selectbox(
        "Select Analysis Option",
        ["Show Data", "Summary Statistics", "Correlation Heatmap", "Sales by Store", "Sales by Holiday Flag"]
    )

    # Perform analysis based on the selected option
    if analysis_option == "Show Data":
        st.header("Dataset")
        st.write(data)

    elif analysis_option == "Summary Statistics":
        st.header("Summary Statistics")
        st.write(data.describe())

    elif analysis_option == "Correlation Heatmap":
        st.header("Correlation Heatmap")
        plt.figure(figsize=(10, 8))
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        st.pyplot()

    elif analysis_option == "Sales by Store":
        st.header("Sales by Store")
        sales_by_store = data.groupby("Store")["Weekly_Sales"].sum().reset_index()
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Store", y="Weekly_Sales", data=sales_by_store)
        plt.xlabel("Store")
        plt.ylabel("Total Weekly Sales")
        plt.title("Total Weekly Sales by Store")
        st.pyplot()

    elif analysis_option == "Sales by Holiday Flag":
        st.header("Sales by Holiday Flag")
        sales_by_holiday = data.groupby("Holiday_Flag")["Weekly_Sales"].sum().reset_index()
        sales_by_holiday["Holiday_Flag"] = sales_by_holiday["Holiday_Flag"].map({0: "Non-Holiday", 1: "Holiday"})
        plt.figure(figsize=(6, 4))
        sns.barplot(x="Holiday_Flag", y="Weekly_Sales", data=sales_by_holiday)
        plt.xlabel("Holiday Flag")
        plt.ylabel("Total Weekly Sales")
        plt.title("Total Weekly Sales by Holiday Flag")
        st.pyplot()
