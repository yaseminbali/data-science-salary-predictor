# app.py
import streamlit as st
import pickle
import pandas as pd

# Loading the model
model = pickle.load(open('salary_model.pkl', 'rb'))

# Streamlit page
st.title('Data Science Salary Predictor')

st.write("""
Enter your qualifications below to estimate your predicted salary.
""")

# User Inputs
education_code = st.selectbox('Education Level Code', [0,1,2,3,4,5,6])
job_code = st.selectbox('Job Title Code', [0,1,2,3,4,5,6,7,8,9,10,11,12,13])
ml_code = st.selectbox('Years of ML Experience Code', [0,1,2,3,4,5,6])
code_years = st.selectbox('Years Coding Code', [0,1,2,3,4,5,6])
uses_python = st.checkbox('Uses Python')
uses_sql = st.checkbox('Uses SQL')
uses_tensorflow = st.checkbox('Uses TensorFlow')

# Mapping checkboxes to 0 or 1
python_flag = 1 if uses_python else 0
sql_flag = 1 if uses_sql else 0
tensorflow_flag = 1 if uses_tensorflow else 0

# Making a dataframe for the input
input_features = pd.DataFrame([[education_code, job_code, ml_code, code_years, python_flag, sql_flag, tensorflow_flag]],
                               columns=['Education_Code', 'Job_Code', 'ML_Code', 'Code_Years', 'Uses_Python', 'Uses_SQL', 'Uses_TensorFlow'])

# Predicting time
predicted_salary = model.predict(input_features)

# Displaying the data
st.subheader(f'Predicted Salary: ${int(predicted_salary[0]):,}')