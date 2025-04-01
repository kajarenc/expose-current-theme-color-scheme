import streamlit as st

st.write(
    f"Your current theme color scheme is: **:rainbow[{st.context.theme_color_scheme}]**"
)


x = st.slider("Enter a number", 0, 20, 0)
st.write(f"Your current slider value is: {x}")
