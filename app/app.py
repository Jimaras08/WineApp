import streamlit as st
import pandas as pd
import requests
import json

st.title('Wine Quality Web App')
st.write('Highly recommend to let Dimi predict the quality of wine before purchase. Happy wife happy life!')

fixed_acidity = st.sidebar.slider(label = 'Fixed Acidity', min_value = 4.0,
                          max_value = 16.0 ,
                          value = 10.0,
                          step = 0.1)

volatile_acidity = st.sidebar.slider(label = 'Volatile Acidity', min_value = 0.00,
                          max_value = 2.00 ,
                          value = 1.00,
                          step = 0.01)
                          
citric_acid = st.sidebar.slider(label = 'Citric Acid', min_value = 0.00,
                          max_value = 1.00 ,
                          value = 0.50,
                          step = 0.01)                          

residual_sugar = st.sidebar.slider(label = 'Residual Sugar', min_value = 0.0,
                          max_value = 16.0 ,
                          value = 8.0,
                          step = 0.1)

chlorides = st.sidebar.slider(label = 'Chlorides', min_value = 0.000,
                          max_value = 1.000 ,
                          value = 0.500,
                          step = 0.001)
   
f_sulf_diox = st.sidebar.slider(label = 'Free Sulfur Dioxide', min_value = 1,
                          max_value = 72,
                          value = 36,
                          step = 1)

t_sulf_diox = st.sidebar.slider(label = 'Total Sulfur Dioxide', min_value = 6,
                          max_value = 289 ,
                          value = 144,
                          step = 1)

density = st.sidebar.slider(label = 'Density', min_value = 0.0000,
                          max_value = 2.0000 ,
                          value = 0.9900,
                          step = 0.0001)

ph = st.sidebar.slider(label = 'pH', min_value = 2.00,
                          max_value = 5.00 ,
                          value = 3.00,
                          step = 0.01)
                          
sulphates = st.sidebar.slider(label = 'Sulphates', min_value = 0.00,
                          max_value = 2.00,
                          value = 0.50,
                          step = 0.01)

alcohol = st.sidebar.slider(label = 'Alcohol', min_value = 8.0,
                          max_value = 15.0,
                          value = 10.5,
                          step = 0.1)


features = {'fixed_acidity': fixed_acidity, 'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid, 'residual_sugar': residual_sugar,
            'chlorides': chlorides, 'free_sulfur_dioxide': f_sulf_diox,
            'total_sulfur_dioxide': t_sulf_diox, 'density': density,
            'pH': ph, 'sulphates': sulphates, 'alcohol': alcohol
            }

features_df  = pd.DataFrame([features])
st.table(features_df)  

if st.button("Predict"):
    response = requests.post('https://rb-ns-wine.herokuapp.com/predict', json.dumps(features))
    st.write(f"Based on feature values, your wine quality is "+str(response.json()))

# local development: streamlit run app.py