import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open('salary_model.pkl', 'rb'))

# Streamlit page
st.title('Data Science Salary Predictor')

st.write("""
Enter your qualifications below to estimate your predicted salary.
""")

# Education Level Key
st.write("""
**Education Level Codes:**
- 0 = Less than a Bachelor's degree
- 1 = Bachelor's degree
- 2 = Master's degree
- 3 = Doctoral degree
- 4 = Professional degree
- 5 = Some college courses
- 6 = Other
""")
education_code = st.selectbox('Education Level Code', [0,1,2,3,4,5,6])

# Job Title Key
st.write("""
**Job Title Codes:**
- 0 = Data Scientist
- 1 = Machine Learning Engineer
- 2 = Data Analyst
- 3 = Research Scientist
- 4 = Software Engineer
- 5 = Data Engineer
- 6 = Statistician
- 7 = Student
- 8 = DBA/Database Engineer
- 9 = Business Analyst
- 10 = Developer Advocate
- 11 = Manager/Executive
- 12 = Educator/Teacher/Professor
- 13 = Consultant
""")
job_code = st.selectbox('Job Title Code', list(range(14)))

# Machine Learning Experience Key
st.write("""
**Years of Machine Learning Experience Codes:**
- 0 = Less than 1 year
- 1 = 1-2 years
- 2 = 2-3 years
- 3 = 3-4 years
- 4 = 4-5 years
- 5 = 5-10 years
- 6 = More than 10 years
""")
ml_code = st.selectbox('Years of ML Experience Code', list(range(7)))

# Coding Experience Key
st.write("""
**Years of Coding Experience Codes:**
- 0 = Less than 1 year
- 1 = 1-2 years
- 2 = 2-3 years
- 3 = 3-5 years
- 4 = 5-10 years
- 5 = 10-20 years
- 6 = 20+ years
""")
code_years = st.selectbox('Years Coding Code', list(range(7)))

# Region Code Key
st.write("""
**Region Codes:**
- 0 = United States
- 1 = India
- 2 = Europe (UK, Germany, France, etc.)
- 3 = Other Asia (China, Japan, Singapore)
- 4 = Other Regions (Africa, South America, Middle East, etc.)
""")
region_code = st.selectbox('Region Code', list(range(5)))

# Technical Tools Checkboxes
uses_python = st.checkbox('Uses Python')
uses_sql = st.checkbox('Uses SQL')
uses_tensorflow = st.checkbox('Uses TensorFlow')

# Mapping checkboxes to 0 or 1
python_flag = 1 if uses_python else 0
sql_flag = 1 if uses_sql else 0
tensorflow_flag = 1 if uses_tensorflow else 0

# Creating dataframe for model input
input_features = pd.DataFrame([[education_code, job_code, ml_code, code_years, 
                                python_flag, sql_flag, tensorflow_flag, region_code]],
                               columns=['Education_Code', 'Job_Code', 'ML_Code', 'Code_Years', 
                                        'Uses_Python', 'Uses_SQL', 'Uses_TensorFlow', 'Region_Code'])

# Predicting salary
predicted_salary = model.predict(input_features)

# Displaying the result
st.subheader(f'Predicted Salary: ${int(predicted_salary[0]):,}')