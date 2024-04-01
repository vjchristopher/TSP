import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title('Spectrum Holding of Different Telecom Operators')


#read in the file
holding = pd.read_csv("spectrum_holding.csv")
holding.LSA=holding.LSA.fillna(method='ffill')

lsa_list=holding['LSA'].unique().tolist()
tsp_list=holding['TSP'].unique().tolist()
band_list=holding.columns.unique().tolist()[2:]


#create a multiselect widget to display genre
LSAS= st.multiselect('Choose LSA:',options=lsa_list, default = ['Andhra Pradesh'])
BANDS=st.multiselect('Choose the Bands:',options=band_list, default = ['700 MHz band (paired)'])
TSPS=st.selectbox('Choose the TSP',tsp_list)

    
if (st.button("Show the holding")):
    df=holding.loc[:,['LSA','TSP']+ BANDS]
    df=df.query('LSA in @LSAS & TSP in @TSPS').reset_index(drop=True)
    st.dataframe(df)
    
    
