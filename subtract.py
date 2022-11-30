import streamlit as st

st.title('Subtraction of 2 given numbers')
st.header('Enter two digit to subtract')
def subtract(dig1,dig2):
    return (dig1-dig2)

number1 = st.number_input('Enter first number')
number2=st.number_input('Enter second number')
st.write('The differnece between number1 and number2 is ', subtract(number1,number2))


st.write('Created by Deepak Sirohiwal (21f1005692)')