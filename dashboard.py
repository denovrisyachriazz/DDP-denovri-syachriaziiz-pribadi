import streamlit as st

st.title("Ini Halaman dashboard!")
st.session_state['nabung']

jumlah = 0
for session in st.session_state['nabung']:
    jumlah += session ['Nominal']

st.write("Total nominal menabung sebesar", jumalah)