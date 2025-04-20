
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Streamlit page setup
st.set_page_config(page_title="USD vs Yield Dashboard v2", layout="wide")

# Optional simple styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        background-color: #ffffff;
    }
    h1, h2, h3 {
        color: #003366;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 USD Index & 10-Year Yield Dashboard (Classic Colors)")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("bilak_anastasiia_dawai_week01_ftdata.csv", parse_dates=["Date"])
    return df

df = load_data()

# Sidebar: date filter
st.sidebar.header("Filter by Date")
min_date = df['Date'].min()
max_date = df['Date'].max()

start_date = st.sidebar.date_input("Start date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End date", max_date, min_value=min_date, max_value=max_date)

# Filter data
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

color_usd = '#1f77b4'   # Blue
color_yield = '#d62728' # Red

ax1.set_xlabel('Date')
ax1.set_ylabel('US Dollar Index', color=color_usd)
ax1.plot(filtered_df['Date'], filtered_df['USD_Index'], color=color_usd, label='US Dollar Index')
ax1.tick_params(axis='y', labelcolor=color_usd)

ax2 = ax1.twinx()
ax2.set_ylabel('10-Year US Yield (%)', color=color_yield)
ax2.plot(filtered_df['Date'], filtered_df['Yield_10Y'], color=color_yield, label='10Y Yield')
ax2.tick_params(axis='y', labelcolor=color_yield)

# Liberation day marker (more transparent)
liberation_day = datetime(2025, 4, 11)
ax1.axvline(x=liberation_day, color='gray', linestyle='--', alpha=0.5, linewidth=1.5, label='Liberation Day')

# Title and legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.title("The dollar usually moves in lockstep with US yields... until 'liberation day'")

st.pyplot(fig)
