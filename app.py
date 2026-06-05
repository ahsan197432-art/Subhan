import streamlit as st
import pandas as pd

from filters import apply_filters
from charts import (
    pie_chart,
    histogram_chart,
    line_chart,
    bar_chart,
    scatter_chart,
    box_plot,
    heatmap_chart,
    area_chart,
    count_plot,
    violin_plot
)

st.set_page_config(
    page_title="Formula 1 Dashboard",
    layout="wide"
)

st.title("🏎 Formula 1 Race Analytics Dashboard")
st.markdown("Interactive dashboard for Formula 1 race performance analysis.")

# Load Data
df = pd.read_csv("data/PROJECT EDA.csv")

# Apply Filters
filtered_df = apply_filters(df)

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(filtered_df))
col2.metric("Total Drivers", filtered_df["driver_name"].nunique())
col3.metric("Total Constructors", filtered_df["constructor_name"].nunique())
col4.metric("Average Points", round(filtered_df["points"].mean(), 2))

st.divider()

# Charts Layout
c1, c2 = st.columns(2)

with c1:
    pie_chart(filtered_df)

with c2:
    histogram_chart(filtered_df)

c3, c4 = st.columns(2)

with c3:
    line_chart(filtered_df)

with c4:
    bar_chart(filtered_df)

c5, c6 = st.columns(2)

with c5:
    scatter_chart(filtered_df)

with c6:
    box_plot(filtered_df)

c7, c8 = st.columns(2)

with c7:
    area_chart(filtered_df)

with c8:
    count_plot(filtered_df)

st.divider()

heatmap_chart(filtered_df)

st.divider()

violin_plot(filtered_df)