# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:57:20 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open ('C:/Users/HP/MACHINE LEARNING/trainedd_model.sav', 'rb'))

# Creating A Function For Prediction
def diabetes_prediction (input_data):
    


    # change the input to numpy array
    data = np.array (input_data)

    # Reshape the numpy array because we are predicting for just one instance or data point
    input_data_reshaped = data.reshape(1, -1)


    prediction = loaded_model.predict (input_data_reshaped)
    print (prediction)


    if (prediction [0] == 0):
        return 'This Person Is Not Diabetic'
    else:
        return'This Person Is Diabetic. See A Doctor'
        
        
def main ():
    
    # Givin A Title
    st.title ('Diabetes Prediction Web App')
    
    # Getting Inputs From The User
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('Body Mass Index Level')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating A Button for Prediction
    
    if st.button ('Diabetes Test Result'):
        diagnosis = diabetes_prediction ([Pregnancies, Glucose, BloodPressure, SkinThickness, 
                                          Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    

        