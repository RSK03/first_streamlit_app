import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



# import streamlit

streamlit.header('Breakfast Menu')
streamlit.text('🍌🥭Omega 3 & Blueberry Oatmeal')
streamlit.text('🥝🍇Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled 🥝🍇Free-Range Egg')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)

# streamlit.header("Fruityvice Fruit Advice!")
# fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
# streamlit.write('The user entered ', fruit_choice)
# # import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# # streamlit.text(fruityvice_response.json())

# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("please select a fruit to get information")
#   else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#   streamlit.error()  

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
    streamlit.stop()
# import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * FROM  FRUIT_LOAD_LIST")
# # my_data_row = my_cur.fetchone()
# # streamlit.header("The fruit load list contains:")
# # streamlit.dataframe(my_data_row)
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("SELECT * FROM  FRUIT_LOAD_LIST")
         return my_cur.fetchall()
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
if streamlit.button('Get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)    

#select * from pc_rivery_db.public.fruit_load_list
# add_my_fruit = streamlit.text_input('what fruit would you like to add?','jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)
# my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

# def insert_row_snowflake(new_fruit):
#     with my_cnx.cursor() as my_cur:
#          my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
#          return "Thanks for adding" + new_fruit

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into FRUIT_LOAD_LIST values ('"+ papaya +"')")
         return "Thanks for adding" + new_fruit
    
add_my_fruit = streamlit.text_input('what fruit would you like to add?','jackfruit')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
