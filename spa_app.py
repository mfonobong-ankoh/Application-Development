
import streamlit as st
from PIL import Image

img = Image.open ("Bella shop.jpg")
st.image(img)

st. header ("Bella's Spa")

st.write("Welcome to Bella's Spa, Please fill the information below to book an appointment with us.")


service = st.radio("What would you like to do today?",["Massage","Pedicure","Manicure"])
          
time = st.time_input("What time would you like to book?")

date = st.date_input("Pick your preffered date?")

name = st.text_input("What is your name")

gender = st.selectbox("Gender",["Male","Female"])


if st.button("Kindly confirm your appointment"):
    st.write(f"Thank you, {name}! You have booked a {service} with us for on the {date} by  {time}.")
    st.write("We look forward to having you!")
else:
    
    st.write("No problem. Please feel free to look through our page for any service you may like to book for in future. Thank you for stopping by.")

