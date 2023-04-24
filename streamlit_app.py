import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Specials                  🥣 🥗 🐔 🥑 🍞               Breakfast ')
streamlit.text('🥗 Special English Breakfast                     🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Made with Love Eggs Benedict                  🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🥑 Health Freak Bowl                             🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
