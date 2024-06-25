import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


def create_item(name: str):
    response = requests.post(f"{BASE_URL}/items", params={"name": name})
    return response.json()


def get_item(item_id: int):
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    return response.json()


st.title("FastAPI and Streamlit Integration")
st.header("Create a new item")
name = st.text_input("Item name")
if st.button("Create item"):
    result = create_item(name)
    st.write(result)

st.header("Get an item")
item_id = st.number_input("Enter the item id", min_value=1, step=1)
if st.button("Get an item"):
    result = get_item(item_id)
    st.write(result)
