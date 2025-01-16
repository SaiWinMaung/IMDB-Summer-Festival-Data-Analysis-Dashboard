import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.express as px


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
        <div style="background-color:  #c2d6d6; border-radius: 8px; text-align: center;">
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
            <div style="background-color:  #c2d6d6; border-radius: 8px; text-align: center;">
            <h4>{title}</h4>
            <p style = "font-size:30px; font-weight: bold;">{df_selection.shape[0]} </p>
            </div>
            """,
                unsafe_allow_html=True,
            )

        if type == "movie":
            Card("Total Number of Movie")
        elif type == "film":
            Card("Total Number of Film")
        else:
            Card("Total Number of Video")

    st.divider()
    st.markdown("## Top 10 Maximum or Minimum Movie, Film and Video")
    selected_columns = ["primary_title", "runtime_minutes"]
    result = df_selection[selected_columns]
    max_or_min = st.radio(
        "Please choose Maximum or Minimum runtime", ["max", "min"], horizontal=True
    )

    if max_or_min == "max":

        def render_mini_bar_chart(value, max_value, width=80, height=5):
            fig, ax = plt.subplots(figsize=(width / 80, height / 80))
            ax.barh([0], [value], color="#c2d6d6", height=0.8)
            ax.set_xlim(0, max_value)
            ax.axis("off")
            buffer = BytesIO()
            plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0)
            plt.close(fig)
            buffer.seek(0)
            return buffer

        sorted_df = result.sort_values(by="runtime_minutes", ascending=False)

        top_10_df = sorted_df.head(10)
        max_value = top_10_df["runtime_minutes"].max()

        title1, title2, title3 = st.columns([2, 1, 3])
        title1.markdown(
            f"""
                <h3 style =" text-align: center;"> Title</h3>""",
            unsafe_allow_html=True,
        )
        title2.markdown(
            f"""
                <h3 style =" text-align: center;"> Minutes</h3>""",
            unsafe_allow_html=True,
        )
        title3.markdown(
            f"""
                <h3 style =" text-align: center;"> Bar Chart</h3>""",
            unsafe_allow_html=True,
        )
        for index, row in top_10_df.iterrows():
            text = row["primary_title"]
            value = row["runtime_minutes"]
            bar_chart = render_mini_bar_chart(value, max_value)

            # Render the row with text, value, and bar chart
            col1, col2, col3 = st.columns([2, 1, 2])
            col1.write(text)
            col2.markdown(
                f"""<p style = "font-color: black;">{value}</p> """,
                unsafe_allow_html=True,
            )
            col3.image(bar_chart, use_container_width=True)

    else:

        def render_mini_bar_chart(value, max_value, width=80, height=5):
            fig, ax = plt.subplots(figsize=(width / 80, height / 80))
            ax.barh([0], [value], color="#c2d6d6", height=0.8)
            ax.set_xlim(0, max_value)
            ax.axis("off")
            buffer = BytesIO()
            plt.savefig(buffer, format="png", bbox_inches="tight", pad_inches=0)
            plt.close(fig)
            buffer.seek(0)
            return buffer

        sorted_df = result.sort_values(
            by="runtime_minutes",
        )
        top_10_df = sorted_df.head(10)
        max_value = top_10_df["runtime_minutes"].max()
        title1, title2, title3 = st.columns([2, 1, 3])
        title1.markdown(
            f"""
                <h3 style =" text-align: center;"> Title</h3>""",
            unsafe_allow_html=True,
        )
        title2.markdown(
            f"""
                <h3 style =" text-align: center;"> Minutes</h3>""",
            unsafe_allow_html=True,
        )
        title3.markdown(
            f"""
                <h3 style =" text-align: center;"> Bar Chart</h3>""",
            unsafe_allow_html=True,
        )
        for index, row in top_10_df.iterrows():
            text = row["primary_title"]
            value = row["runtime_minutes"]
            bar_chart = render_mini_bar_chart(value, max_value)

            # Render the row with text, value, and bar chart
            col1, col2, col3 = st.columns([2, 1, 2])
            col1.write(text)
            col2.markdown(
                f"""
                <p style = "font-color : red; ">{value}</p>""",
                unsafe_allow_html=True,
            )
            col3.image(bar_chart, use_container_width= True)

    # for unique genre
    st.divider()
    st.markdown("## Genres with Pie Chart")
    __, pie1, __ = st.columns([0.5, 3, 0.5])
    with pie1:
        df_selection["genres_List"] = df_selection["genres"].apply(
            lambda x: [genre.strip() for genre in x.split(",")]
        )

        # Flatten all genres into a single list
        all_genres = [
            genre for sublist in df_selection["genres_List"] for genre in sublist
        ]

        # Get unique genres with their counts
        genre_counts = pd.Series(all_genres).value_counts()
        
        top_genres = genre_counts.head(5)
        
        
        fig, ax = plt.subplots(figsize=(3, 3),)  # Adjust the figure size
        wedges, texts, autotexts = ax.pie(
            top_genres,
            labels=None,  # Hide labels on the pie
            autopct="%1.1f%%",  # Show percentages
            startangle=140,
            textprops={"fontsize": 8},
            colors= ['#a3c2c2','#ff6666','#e6e600','#80d4ff','#ffd966']
        )

        ax.legend(
            wedges,
            top_genres.index,
            title="Genres",
            loc="lower left",
            bbox_to_anchor=(1, 0.5),
            fontsize=6,
        )

        # Ensure the pie chart is circular
        ax.axis("equal")

        st.pyplot(fig)
    
    st.divider()
    line_df= df_selection[['year','average_rating','num_votes']]
    st.markdown('## Rating over the year')
    st.line_chart(line_df, x= 'year', y = 'average_rating', x_label='Year', y_label='Rating' , color= '#cccc00')

    st.divider()
    st.markdown('## Votes over the year')
    st.line_chart(line_df, x= 'year', y = 'num_votes', x_label='Year', y_label='Votes' , color= '#cccc00')