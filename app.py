import streamlit as st

st.write(
    f"Your current theme color scheme is: **:rainbow[{st.context.theme_color_scheme}]**"
)

st.write("And here is dog image:")

if st.context.theme_color_scheme == "light":
    st.image("doglight.jpg")
else:
    st.image("dogdark.jpg")


x = st.slider("Enter a number", 0, 20, 0)
st.write(f"Your current slider value is: {x}")
