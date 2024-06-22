import streamlit as st

st.title("Title")
st.header("header")
st.subheader("subheader")
st.write("Write Something")

if st.button("1 + 1"):
    st.write("2!!!")

if st.button("1 + 2"):
    st.write("3!!!")

selected_items = st.radio('Radio Part', ('A', 'B', 'C'))

st.write(selected_items + "!!!")