import streamlit as st
import langchain_helper #custom module from the same directory, no need

st.title("Restaurant Name & Menu Generator")

cuisine= st.sidebar.selectbox("Select a cuisine", ["Indian", "Chinese", "Italian", "Mexican", "American"])

# def generate_rstaurant_name_and_item(cuisine):
#     return{
#         'restaurant_name': 'Curry delight',
#         'menu': 'Butter chicken, Tandoori chicken, Naan, Paneer butter masala'
#     }

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_item(cuisine)  #called langchain_helper.py

    st.header(response['restaurant_name'].strip())
    menu_items = response['menu'].strip().split(',')  # split function is iused to covert comma separated string to list

    st.write("**Menu Items**")
    for i in menu_items:
        st.write("-", i)
