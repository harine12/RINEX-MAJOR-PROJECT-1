import streamlit as st
import joblib
import pandas
model = joblib.load('Linear regression model')
st.title('LINEAR REGRESSION MODEL FOR PRICE OF USED CARS')

year = st.number_input("year", min_value=1996, max_value=2060)
mileage = st.number_input("mileage", min_value=1, max_value=200000)
tax = st.number_input("tax in euros", min_value=0, max_value=600)
mpg = st.number_input("miles per gallon", min_value=10, max_value=203)
engineSize = st.number_input("Engine size in litres", min_value=1.0, max_value=5.0, step=1., format="%.2f")

input_data = [[year, mileage, tax, mpg, engineSize]]
pred = model.predict(input_data)

if st.button('Predict car price (in euros)'):
  st.subheader(pred)
