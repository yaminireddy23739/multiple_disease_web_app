# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 00:42:57 2023

@author: Yamini
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
                    
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

breast_cancer_model = pickle.load(open('breast_cancer_model.sav','rb'))



# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons = ['activity','heart','person','file-medical'],
                           
                           default_index=0,)
    
    
# Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML') 
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    
    with col2:
        Insulin = st.number_input('Insulin Level')
    
    with col3:
        BMI = st.number_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

    

# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    # page title
   st.title('Heart Disease Prediction using ML')
   
   
   col1, col2, col3 = st.columns(3)
   
   with col1:
       age = st.number_input('Age')
       
   with col2:
       sex = st.number_input('Sex')
       
   with col3:
       cp = st.number_input('Chest Pain types')
       
   with col1:
       trestbps = st.number_input('Resting Blood Pressure')
       
   with col2:
       chol = st.number_input('Serum Cholestoral in mg/dl')
       
   with col3:
       fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
       
   with col1:
       restecg = st.number_input('Resting Electrocardiographic results')
       
   with col2:
       thalach = st.number_input('Maximum Heart Rate achieved')
       
   with col3:
       exang = st.number_input('Exercise Induced Angina')
       
   with col1:
       oldpeak = st.number_input('ST depression induced by exercise')
       
   with col2:
       slope = st.number_input('Slope of the peak exercise ST segment')
       
   with col3:
       ca = st.number_input('Major vessels colored by flourosopy')
       
   with col1:
       thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
       
       
    
   # code for Prediction
   heart_diagnosis = ''
   
   # creating a button for Prediction
   
   if st.button('Heart Disease Test Result'):
       heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
       
       if (heart_prediction[0] == 1):
         heart_diagnosis = 'The person is having heart disease'
       else:
         heart_diagnosis = 'The person does not have any heart disease'
       
   st.success(heart_diagnosis)
       
    

# Parkinsons Prediction Page
if (selected == 'Parkinsons Prediction'):
    
    # page title
    st.title('Parkinsons Prediction using ML')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.number_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.number_input('MDVP: RAP')
        
    with col2:
        PPQ = st.number_input('MDVP: PPQ')
        
    with col3:
        DDP = st.number_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.number_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP: Shimmer(dB)')
        
    with col1:
        APQ3 = st.number_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.number_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.number_input('MDVP: APQ')
        
    with col4:
        DDA = st.number_input('Shimmer: DDA')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('spread1')
        
    with col5:
        spread2 = st.number_input('spread2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
        
        # page title
        st.title('Breast Cancer Prediction using ML')
        
        
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            mean_radius = st.number_input('Radius_mean')
            
        with col2:
            mean_texture = st.number_input('Texture_mean')
            
        with col3:
            mean_perimeter = st.number_input('Perimeter_mean')
            
        with col4:
            mean_area = st.number_input('Area_mean')
            
        with col5:
            mean_smoothness = st.number_input('Smoothness_mean')
            
        with col6:
            mean_compactness = st.number_input('Compactness_mean')
            
        with col1:
            mean_concavity = st.number_input('Concavity_mean')
            
        with col2:
            mean_concave_points = st.number_input('Concave_points_mean')
            
        with col3:
            mean_symmetry = st.number_input('Symmetry_mean')
        
        with col4:
            mean_fractal_dimension = st.number_input('Fractal_dimension_mean')
            
        with col5:
            radius_error = st.number_input('Radius_se')
            
        with col6:
            texture_error = st.number_input('Texture_se')
            
        with col1:
            perimeter_error = st.number_input('Perimeter_se')
                
        with col2:
            area_error = st.number_input('Area_se')
                
        with col3:
            smoothness_error = st.number_input('Smoothness_se')
            
        with col4:
            compactness_error = st.number_input('Compactness_se')
                
        with col5:
            concavity_error = st.number_input('Concavity_se')
                
        with col6:
            concave_points_error = st.number_input('Concave_points_se')
                
        with col1:
            symmetry_error = st.number_input('Symmetry_se')
                    
        with col2:
            fractal_dimension_error = st.number_input('Fractal_dimension_se')
                    
        with col3:
            worst_radius = st.number_input('Radius_worst')
                
        with col4:
            worst_texture = st.number_input('Texture_worst')
                    
        with col5:
            worst_perimeter = st.number_input('Perimeter_worst')
                    
        with col6:
            worst_area = st.number_input('Area_worst')
                    
        with col1:
            worst_smoothness = st.number_input('Smoothness_worst')
                        
        with col2:
            worst_compactness= st.number_input('Compactness_worst')
                        
        with col3:
            worst_concavity = st.number_input('Concavity_worst')
                    
        with col4:
            worst_concave_points = st.number_input('Concave_points_worst')
                        
        with col5:
            worst_symmetry = st.number_input('Symmetry_worst')
                        
        with col6:
            worst_fractal_dimension = st.number_input('Fractal_dimension_worst')
            
            
            
        # code for Prediction
        breast_cancer_diagnosis = ''
            
        # creating a button for Prediction
            
        if st.button("Breast Cancer Test Result"):
            breast_cancer_prediction = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter,mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])                          
                
            if (breast_cancer_prediction[0] == 1):
                breast_cancer_diagnosis = "The person has breast cancer"
            else:
                breast_cancer_diagnosis = "The person does not have breast cancer"
               
        st.success(breast_cancer_diagnosis)
               





    
    
    
