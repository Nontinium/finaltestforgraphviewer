import streamlit as st

with open("my_final_applicationtest_1.0.0.exe", "rb") as file:
    btn = st.download_button(
        label="Download program",
        data=file,
        file_name="my_final_applicationtest_1.0.0.exe",
        mime="image/png",
    )
