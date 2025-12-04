import streamlit as st
from app.predict import predict

st.title("Cirrhosis Death Predictor SUML")

# create empty dictionary
user_input = {}

int_features = [
    'N_Days', 'Age', 'Stage', 'Platelets'
]

float_features = [
    'Bilirubin', 'Cholesterol', 'Albumin', 'Copper',
    'Alk_Phos', 'SGOT', 'Tryglicerides', 'Prothrombin'
]

binary_features = [
    'Drug_Placebo', 'Sex_M', 'Ascites_Y',
    'Hepatomegaly_Y', 'Spiders_Y', 'Edema_S', 'Edema_Y'
]

# ordered union
feature_order = int_features + float_features + binary_features

for feature in feature_order:
    if feature in binary_features:
        user_input[feature] = st.selectbox(f"{feature} (0=No, 1=Yes)", [0, 1])
    elif feature in int_features:
        user_input[feature] = st.number_input(feature, value=0, step=1, format="%d")
    else:
        user_input[feature] = st.number_input(feature, value=0.0)



if st.button("Predict"):
    result = predict(user_input)
    if result == 1:
        st.error("Prediction: DEAD")
    else:
        st.success("Prediction: ALIVE")
