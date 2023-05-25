import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "Superstore Dashboard",
    layout="wide"
)
df = pd.read_csv('data/superstore.csv')
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime(df['ship_date'])

st.title("Superstore Dashboard")

st .dataframe(df)


df['order_year'] = df['order_date'].dt.year
CURR_YEAR = df['order_year'].max()
PREV_YEAR = CURR_YEAR - 1

mx_data = pd.pivot_table(
    data=df, 
    index='order_year',
    aggfunc={
        'sales':np.sum,
        'profit':np.sum,
        'order_id':pd.Series.nunique,
        'customer_id':pd.Series.nunique
    }
).reset_index()
mx_data['profit_ratio'] = 100.0 * mx_data['profit']/mx_data['sales']