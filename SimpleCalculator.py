import streamlit as st

st.title("Simple Calculator")

st.write("Addition | Subtraction")

first_number = st.number_input("Enter first Number")
choose = st.selectbox("Choose an operator:", ["+", "-"])
second_number = st.number_input("Enter second Number")

calculate = None

if st.button("Calculate"):
    if choose == "+":
        calculate = first_number + second_number
    else:
        calculate = first_number - second_number

if calculate is not None:
    st.success(f"Your Answer is: {calculate}")