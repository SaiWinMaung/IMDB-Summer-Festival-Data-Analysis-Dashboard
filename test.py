import streamlit as st
import pandas as pd
import altair as alt

# Sample data
data = {
    "year": [2018, 2019, 2020, 2021, 2022],
    "rating": [7.5, 8.0, 7.0, 9.0, 9.5],
    "votes": [1200, 1500, 1800, 2000, 2500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format for easier plotting
df_melted = df.melt(id_vars="year", value_vars=["rating", "votes"], var_name="Metric", value_name="Value")

# Streamlit app
st.title("Line Chart Example")
st.write("Displaying a line chart with `year` on the x-axis and `rating` and `votes` as two separate lines.")

# Plot using Altair
chart = alt.Chart(df_melted).mark_line(point=True).encode(
    x=alt.X("year:O", title="Year"),  # Year as an ordinal value
    y=alt.Y("Value:Q", title="Values"),
    color="Metric:N",  # Different lines for 'rating' and 'votes'
    tooltip=["year", "Metric", "Value"]  # Tooltips for interactivity
).properties(
    width=700,
    height=400,
    title="Ratings and Votes Over the Years"
)

st.altair_chart(chart, use_container_width=True)
