import streamlit as st
from PIL import Image

# Set page title and background color
st.set_page_config(page_title="Happy Rose Day 🌹", page_icon="🌹", layout="centered")

# Display Rose Image
st.markdown("<h1 style='text-align: center; color: #D80032;'>🌹 Happy Rose Day 🌹</h1>", unsafe_allow_html=True)
rose_image = Image.open("rose.jpg")  # Make sure 'rose.jpg' is in the same folder
st.image(rose_image, use_column_width=True)

# Display Rose Day Message
st.markdown(
    """
    <div style="text-align: center; font-size: 20px; color: #800000;">
        A rose is not just a flower, it is a symbol of love, joy, and friendship. <br><br>
        May this beautiful Rose Day bring happiness and love into your life. 🌷💖
    </div>
    """,
    unsafe_allow_html=True
)

# Button to Show a Popup Message
if st.button("Spread Love 💖"):
    st.success("Happy Rose Day, Gulsha! 🌹 May your life be filled with love and happiness!")

