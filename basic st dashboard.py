

# relevant packages
import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import base64

# UI =====================
st.title('Hey GitHub viewer')
st.header("Financial dashboard")
         
#               ***
# Some UI stuff if you want
# =============================================================================
# main_bg ="...jpg"
# main_bg_ext = "jpg"
# 
# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
# 
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# =============================================================================


#  sidebar: ================
# Add a selectbox to the sidebar:

add_selectbox = st.sidebar.selectbox(
    'What algorithm should we use?',
    ('Knn', 'CNN', 'DT')
)

# END sidebar: ================




# list of possible stocks
tickers = ("ABG","BTC-USD",
           "MTN",
           "SLM",
           "VOD")
# DROPDOWN

add_selectbox_ass = st.sidebar.selectbox(
    'What assets are you interested in?',
    tickers
)
#dates

start = st.sidebar.date_input("Start date",
                      value=pd.to_datetime("2021-01-01"))
end = st.sidebar.date_input("End date",
                      value=pd.to_datetime("today"))






def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod()-1
    cumret = cumret.fillna(0)
    return cumret
    
    
    
# online data req
# plot price before the return

if len(add_selectbox_ass)>0:
    
    # iow choose asset
    #df=yf.download(dropdown, start,end)["Adj Close"]
    #st.line_chart(df)
    df = relativeret(yf.download(add_selectbox_ass, start,end)["Adj Close"])
    st.header("Cumulative Returns van {}".format(add_selectbox_ass))
    st.area_chart(df)
    
    df2=yf.download(add_selectbox_ass, start,end)["Adj Close"]
    st.header("Adj Close van {}".format(add_selectbox_ass))
    st.line_chart(df2)
    
    @st.cache(allow_output_mutation=True)
    def get_dataframe():
        return pd.DataFrame()
    

    dfd = get_dataframe()

    # Create row, column, and value inputs
# =============================================================================
#     row = st.number_input('row', max_value=dfd.shape[0])
#     col = st.number_input('column', max_value=dfd.shape[1])
# =============================================================================
    #value = st.number_input('value')
    value = yf.download(add_selectbox_ass, start,end)
    #    Change the entry at (row, col) to the given value
    dfd = value
    # And display the result!
    st.dataframe(dfd)
    n = yf.Ticker(add_selectbox_ass).news
    r = yf.Ticker(add_selectbox_ass).recommendations
    st.dataframe(n)
    r



    
assets = tickers
#Assign weights to the stocks.
 
# for future portofolia management applications
weights = np.array([0.25,0.25,0.25,0.25])

# Randomly fill a dataframe and cache it
# =============================================================================
# @st.cache(allow_output_mutation=True)
# def get_dataframe():
#     return pd.DataFrame(
#         np.random.randn(50, 20),
#         columns=('col %d' % i for i in range(20)))
# 
# 
# df = get_dataframe()
# =============================================================================

# =============================================================================
# # Create row, column, and value inputs
# row = st.number_input('row', max_value=df.shape[0])
# col = st.number_input('column', max_value=df.shape[1])
# value = st.number_input('value')
# 
# # Change the entry at (row, col) to the given value
# df.values[row][col] = value
# 
# # And display the result!
# st.dataframe(df)
# =============================================================================
