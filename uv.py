import streamlit as st
st.title('my first streamlit app')
if st.button("click me"):
    st.write("button clicked")


import streamlit as st
st.title("BMi calculator")
st.markdown("This app calculates the BMI of the person")
weight = st.number_input("Enter your weight in kg")
height = st.number_input("Enter your height in cm")
if st.button("Calculate BMI"):
    bmi = weight / ((height/100)**2)
    st.write("Your BMI is ", bmi)
    if bmi < 18.5:
        st.write("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.write("You are normal weight")
    elif bmi >= 25 and bmi < 30:
        st.write("You are overweight")
    elif bmi >= 30:
        st.write("You are obese")