# streamlit_app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Simple Linear Regression App')

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

# User input
income_level = st.number_input('Enter Income Level:', min_value=0, step=1)

if st.button('Predict'):
    prediction = model.predict(np.array([[income_level]]))
    st.write(f'Predicted Risk: {prediction[0]}')
