# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:50:21 2026

@author: amajid
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('First App')
st.write('This is my first app in streamlit')
name=st.text_input('Plz enter your name')
st.write('you entered',name)
age=st.number_input('enter your age')
st.write('your age is',age)

st.subheader('Slide bar')

value=st.slider('Plese choose from',0,100,50)

st.write('you selected',value)


a=st.selectbox('please choose',[1,2,3,4])

st.write('you chose',a)

data=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
st.dataframe(data)

st.sidebar.title('Available Datasets')

b=st.sidebar.slider('pick a number',1,40,4)

if st.button('Plot graph'):
    
    fig,ax=plt.subplots()
    x=np.linspace(-np.pi,np.pi,100)
    y=np.cos(x)
    
    ax.plot(x,y)
    
    st.pyplot(fig)
        






