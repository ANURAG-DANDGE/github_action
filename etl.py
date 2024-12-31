import streamlit as st
import pandas as pd 
data = {
    'Task': ['Extract', 'Transform', 'Load'],
    'Status': ['Completed', 'InProgress', 'Pending']
    }
df = pd.DataFrame(data)

st.write('ETL Execution : Status 4')
st.write(df)
