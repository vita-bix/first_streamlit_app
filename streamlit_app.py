import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Specials                  🥣 🥗 🐔 🥑 🍞               Breakfast ')
streamlit.text('🥗 Special English Breakfast                     🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Made with Love Eggs Benedict                  🥗 Kale,Spinach & Rocket Smoothie')
streamlit.text('🥑 Health Freak Bowl                             🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# pick list for customers to pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

# display table on page
streamlit.dataframe(my_fruit_list)

