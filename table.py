import streamlit as st
import pandas as pd


def TableView():
    df = pd.read_csv("summer_movies.csv")
    df = df.dropna()
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
    st.markdown(html_title, unsafe_allow_html=True)
    st.dataframe(df)
    num_row = df.shape[0]
    row, rownum = st.columns(2)
    with row:
        st.markdown("***Total Number of Row*** :")

    with rownum:
        st.text(num_row)

    st.write("")
    (
        col,
        colname,
    ) = st.columns(2)
    with col:
        st.markdown("***Column Name*** :")
    with colname:
        for col in df.columns:
            st.text(col)

