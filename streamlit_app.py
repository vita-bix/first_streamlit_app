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
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table on page
streamlit.dataframe(fruits_to_show)


# New section to display fruitvice api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version of the response & normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

