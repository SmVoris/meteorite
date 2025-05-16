import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import pydeck as pdk


st.title('Meteorite Landing Dashboard')

@st.cache(persist=True)
def load_data(nrows): 
    df = pd.read_csv('Meteorite_Landings.csv', nrows=nrows)

    df.dropna(subset=['reclat','reclong'], inplace=True)

    df = df[df['reclat'] != 0]
    df = df[df['reclong'] != 0]
    
    lowercase = lambda x : str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df
df = load_data(100000)

st.map(df[['reclat','reclong']])