import streamlit
streamlit.title('My Family New Healthy Food ')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 omega 3 & Millet Upma')
streamlit.text('broownrice & egg omlet')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
