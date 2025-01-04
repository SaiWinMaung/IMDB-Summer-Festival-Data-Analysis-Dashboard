import streamlit as st
import pandas as pd
import numpy as np
import chart
import table


st.set_page_config(layout= 'wide', page_icon=':popcorn:', page_title='IMDB Summer Movie Dashboard')

st.sidebar.image('movie.jpg', width= 250)
page_option = st.sidebar.selectbox('Please select page option', ['Chart Page', 'Table Page'])


if page_option == 'Chart Page':
    chart.ChartView()
else :
    table.TableView()
