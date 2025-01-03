import streamlit as st
import pandas as pd

def ChartView():
    df = pd.read_csv('summer_movies.csv')
    df =df.dropna()
    image, header = st.columns([0.2, 0.8])
    with image:
        st.image("movie.jpg", width=150,)    
    html_title = """
    <style>
    .title-test{
    font-weight:bold;
    padding: 5px;
    border-radius:6px
    }
    </style>
    <center><h1 class = "title-test"> IMDB Summer Festival Dashboard </h1></center>
    """
    with header:
        st.markdown(html_title, unsafe_allow_html=True)

    st.sidebar.radio('Select Title type', options= df['title_type'].unique())
    