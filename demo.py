import numpy as np
import pandas as pd
import streamlit as st

st.title("DEMO PAGE")
st.write("123")
st.write("## 123")

arr1=np.arry(1,2,3,4,5,6)
st.write(arr1)

df1=pd.DataFrame(〔〔11,22,33,44〕,〔50,60,70,80〕〕)
St.write(df1)                 
st.table(df1)

st.write("## 核取方塊")
1=st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用") 

    checks=st.columns(2)   
txt=‵′
with checks〔0〕:
r11=st.checkbox("外帶")
if r11:
     txt+="A"



                 


