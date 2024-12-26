import streamlit as st
from src.password_generators import PinGenerator,RandomPasswordGenerator,MemorablePasswordGenerator 


st.image("./src/images/banner.jpeg", width= 600)
st.title("Password Generator")

option = st.radio(
    "Select a password generator",
    ("Random Password", "Memorable Password", "Pin Code")
)

if option == 'Pin Code':
    length = st.slider('Select the length of the pin code', 4, 32)

    generator = PinGenerator(length)
    
elif option == 'Random Password':
    length = st.slider('Select the length of the pin password', 8, 50)
    include_symbol = st.toggle("Include symbol")
    include_number = st.toggle("Include Number")

    generator = RandomPasswordGenerator(length, include_number, include_symbol)

elif option == 'Memorable Password':
    num_of_words = st.slider('Select the number of words', 2, 10)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    generator = MemorablePasswordGenerator(num_of_words, separator, capitalization)



password = generator.generate()
st.write(f"Your password is: `{password}`")    