import streamlit as st
import pandas as pd


def ChartView():
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

    st.divider()
    col1, __, col2 = st.columns([0.4, 0.001, 0.3])

    with col1:
        st.markdown(
            f"""
        <div style="background-color:  #c2d6d6; padding: 10px; border-radius: 8px; text-align: center;">
        <h4>Total Number of Movie, Film and Video</h4>
        <p style = "font-size:30px; font-weight: bold;">{df.shape[0]} </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    type = st.sidebar.radio("Select Title type", options=df["title_type"].unique())

    df_selection = df.query("title_type == @type")

    with col2:

        def Card(title):
            st.markdown(
                f"""
            <div style="background-color:  #c2d6d6; padding: 10px; border-radius: 8px; text-align: center;">
            <h4>{title}</h4>
            <p style = "font-size:30px; font-weight: bold;">{df_selection.shape[0]} </p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        if type == "movie":
            Card('Total Number of Movie')
        elif type == "film":
            Card('Total Number of Film')
        else:
            Card('Total Number of Video')
