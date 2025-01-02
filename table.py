import streamlit  as st
import pandas as pd


df = pd.read_csv('summer_movies.csv')
df.dropna(inplace= True)
print(df.isnull().sum())
def TableView() :
    st.title('IMDB Summer Festival Data Table')
    st.write(df)