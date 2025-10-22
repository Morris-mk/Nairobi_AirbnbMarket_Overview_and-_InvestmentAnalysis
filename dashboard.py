import plotly.express as px
import seaborn as sns
import streamlit as st
import pandas as pd 
import numpy as np

st.header(" Nairobi's Airbnb Market Overview & Investment Analysis")

data = pd.read_csv(r'https://github.com/Morris-mk/Nairobi_AirbnbMarket_Overview_and-_InvestmentAnalysis/raw/refs/heads/main/data/listings_raw_data.csv')

st.map(data=data, longitude=data.longitude, latitude=data.latitude)