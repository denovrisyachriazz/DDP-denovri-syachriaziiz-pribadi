import streamlit as st

# st.write('hello world!')

dashboard = st.Page("./Pages/dashboard.py", title="Dashboard")
nabung = st.Page("./Pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung]
})

if "nabung" not in st.session_state:
    st.session_state['nabung']= []

pg.run()
