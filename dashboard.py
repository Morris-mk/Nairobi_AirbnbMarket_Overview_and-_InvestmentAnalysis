import plotly.express as px
import seaborn as sns
import streamlit as st
import pandas as pd 
import numpy as np

# A Dashboard heading and short description
st.header(" Nairobi's Airbnb Market Overview & Investment Analysis Dashboard 📊")

st.markdown("""
## Hello 👋! 
This dashboard, presents a detailed analysis into Nairobi's Airbnb and short-term vacation rentals market, uncovering insights about the distribution, occupancy rates, revenue generation and seasonal trends in the market.

The goal of this analysis is to give you the neccesary information to empower and guide your investment decision and the pricing strategy for your listing. 
It does this by showcasing key insights, patterns and trends about the listings distribution across Nairobi, their occupancy and revenue generation and trends and patterns in market.
            
""")
data = pd.read_csv(r'https://github.com/Morris-mk/Nairobi_AirbnbMarket_Overview_and-_InvestmentAnalysis/raw/refs/heads/main/data/listings_raw_data.csv')


st.checkbox('Show the Listings Data used',
            st.dataframe(data))

# create the summary analytics tiles 
col1, col2, col3 = st.columns(3)


st.subheader("Distribution of Listings across Nairobi")
st.map(data=data, width=600, height=400)


