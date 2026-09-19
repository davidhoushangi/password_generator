import streamlit as st

st.image("banner1.png", width=400)
st.title("Password Generator")

from password_generator import PinGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

option = st.radio("Select a password generator", ("Random Password", "Memorable Password", "Pin Code"))

if option == "Pin Code":
    length = st.slider("Select the pin length", 4, 32)
    generator = PinGenerator(length) 

elif option == "Random Password":
    length = st.slider("Select the password length", 8, 100)
    include_symbol = st.toggle("Include Symbols") 
    include_number = st.toggle("Include Numbers")
    generator = RandomPasswordGenerator(length, include_numbers=include_number, include_symbols=include_symbol)

elif option == "Memorable Password":
    length = st.slider("Select the number of words", 2, 10)
    separator = st.text_input("Separator", value='-') 
    capitalization = st.toggle("Capitalization")
    generator = MemorablePasswordGenerator(number_of_words=length, separator=separator, capitalization=capitalization)

password = generator.generate()
st.write(f"Your password is: `{password}`")
