import streamlit as st
import pandas as pd
import plotly.express as px

# Example data
data = {
    "Genres": ["Drama, Comedy, Action", "Action, Thriller", "Drama, Horror, Comedy"]
}
df = pd.DataFrame(data)

# Split each cell in the 'Genres' column into a list of genres
df['Genres_List'] = df['Genres'].apply(lambda x: [genre.strip() for genre in x.split(',')])

# Flatten all genres into a single list
all_genres = [genre for sublist in df['Genres_List'] for genre in sublist]

# Get unique genres with their counts
genre_counts = pd.DataFrame({'Genre': all_genres}).value_counts().reset_index(name='Count')

# Streamlit app
st.title("Genre Analysis with Pie Chart")

# Display the table of genre counts
st.write("Genre Occurrences:")
st.dataframe(genre_counts)

# Plot a pie chart using Plotly
fig = px.pie(genre_counts, names='Genre', values='Count', title='Genre Distribution')
st.plotly_chart(fig)

# Search for a specific genre and filter
search_term = st.text_input("Enter a genre to search (e.g., 'Action')")
if search_term:
    filtered_df = df[df['Genres_List'].apply(lambda x: search_term.strip().capitalize() in x)]
    st.write(f"Rows containing '{search_term}':")
    st.dataframe(filtered_df)
