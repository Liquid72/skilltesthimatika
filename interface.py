import streamlit as st
import joblib

# Load the model
model = joblib.load('model.pkl')

st.header('Heart Disease Prediction Demo')

age = st.number_input('Enter your age', min_value=0, max_value=90)
sex = st.radio('Select Your Gender',
               ['Male','Female'])

cp = st.selectbox('Select Chest Pain Type',
                    ['Typical Angina','Atypical Angina','Non-anginal Pain','Asymptomatic'])

trestbps = st.number_input('Enter Resting Blood Pressure', min_value=0, max_value=200)
chol = st.number_input('Enter Serum Cholesterol', min_value=0, max_value=600)
fbs = st.radio('Fasting Blood Sugar > 120 mg/dl',['True','False'])
restecg = st.selectbox('Resting Electrocardiographic Results',
                    ['Normal','ST-T wave abnormality','Left ventricular hypertrophy'])
thalach = st.number_input('Enter Maximum Heart Rate Achieved', min_value=0, max_value=200)
exng = st.radio('Exercise Induced Angina',['Yes','No'])
oldpeak = st.number_input('Enter ST Depression induced by exercise relative to rest', min_value=0.0, max_value=10.0)
slp = st.selectbox('Select Slope of the peak exercise ST segment', ['Upsloping','Flat','Downsloping'])
caa = st.selectbox('Number of major vessels (0-3) colored by Flourosopy', [0,1,2,3])
thal = st.selectbox('Thalassemia', ['Normal','Fixed Defect','Reversable Defect'])

if st.button('Predict'):
    # convert sex to binary
    sex = 1 if sex == "Male" else 0
    cp = 0 if cp == "Typical Angina" else 1 if cp == "Atypical Angina" else 2 if cp == "Non-anginal Pain" else 3
    fb = 1 if fbs == "True" else 0
    restecg = 0 if restecg == "Normal" else 1 if restecg == "ST-T wave abnormality" else 2
    exng = 1 if exng == "Yes" else 0
    slp = 0 if slp == "Upsloping" else 1 if slp == "Flat" else 2
    thal = 0 if thal == "Normal" else 1 if thal == "Fixed Defect" else 2

    pred = model.predict([[age,sex,cp,trestbps,chol,fb,restecg,thalach,exng,oldpeak,slp,caa,thal]])[0]
    if pred == 1:
        st.error('You have a heart disease')
    else:
        st.success('You do not have a heart disease')
