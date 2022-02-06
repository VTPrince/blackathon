import pickle
from sympy import Ge, Rel
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pycaret import classification
model = classification.load_model(model_name='gbc')
def predict(Country,Location,Cellphone,Age,Gender,Relation,Marital,Education,Job):
    if Country=="Kenya":
        Country=1
    elif Country=="Rwanda":
        Country=2
    elif Country=="Tanzania":
        Country=3
    else:
        Country=4
    if Location=="Urban":
        Location=2
    else:
        Location=1
    if Cellphone=="Yes":
        Cellphone=True
    else:
        Cellphone=False
    if Gender=="Female":
        Gender=1
    else:
        Gender=2
    if Relation=='Spouse':
        Relation=1
    elif Relation=='Head of Household':
        Relation=2
    elif Relation=='Other relative':
        Relation=3
    elif Relation=='Child':
        Relation=4
    elif Relation=='Parent':
        Relation=5
    else:
        Relation=6
    if Marital=='Married/Living together':
        Marital=1
    elif Marital=='Widowed':
        Marital=2
    elif Marital=='Single/Never Married':
        Marital=3
    elif Marital=='Divorced/Seperated':
        Marital=4
    else:
        Marital=5
    if Education=='Secondary education':
        Education=1
    elif Education=='No formal education':
        Education=2
    elif Education=='Vocational/Specialised training':
        Education=3
    elif Education=='Primary education':
        Education=4
    elif Education=='Tertiary education':
        Education=5
    else:
        Education=6
    if Job=='Self employed':
        Job=1
    elif Job=='Government Dependent':
        Job=2
    elif Job=='Formally employed Private':
        Job=3
    elif Job=='Informally employed':
        Job=4
    elif Job=='Formally employed Government':
        Job=5
    elif Job=='Farming and Fishing':
        Job=6
    elif Job=='Remittance Dependent':
        Job=7
    elif Job=='Other Income':
        Job=8
    elif Job=='Dont Know/Refuse to answer':
        Job=9
    else:
        Job=10
    values=[Country,Location,Cellphone,Age,Gender,Relation,Marital,Education,Job]
    ###features = [float(i) for i in values]
    ###array_features = [np.array(features)]
    prediction = model.predict(values)
    if(prediction == 3):
        st.text("You are safe,there are very low chances of the wildfire reaching your city ")
    elif(prediction == 2):
        st.text("You might be in danger as the wilfire is expected to reach you in 7-10 days, you must prepare to evacuate")
    elif(prediction == 1):
        st.text("You are in danger, the wildfire is expected to reach within 3-7 days,you must evacuate")
    else:
        st.text("Immediate Danger, wildfire might reach your city within 1-3 days, evacuate now!")

def main():

    Country = st.selectbox("Select the name of the country you belong to: ", ("Kenya","Rwanda","Tanzania","Uganda"))
    Location = st.selectbox("Select the type of area you live in: ",("Rural","Urban"))
    Cellphone = st.selectbox("Do you have access to cellphone",("Yes","No"))
    Age = st.number_input("Enter your age")
    Gender = st.selectbox("Select your gender",("Male","Female"))
    Relation = st.selectbox("Select your relationship with the head of your family", ("Spouse","Head of Household","Other relative","Child","Parent","Other non-relatives"))
    Marital = st.selectbox("Select your marital status",("Married/Living together","Widowed","Single/Never Married","Divorced/Seperated","Dont know"))
    Education = st.selectbox("Select your education level",("Secondary education","No formal education","Vocational/Specialised training","Primary education","Tertiary education","Other/Dont know/RTA"))
    Job = st.selectbox("Select your type of job",("Self employed","Government Dependent","Formally employed Private","Informally employed","Formally employed Government","Farming and Fishing","Remittance Dependent","Other Income","Dont Know/Refuse to answer","No Income"))

    if st.button("Predict"):
            predict(Country,Location,Cellphone,Age,Gender,Relation,Marital,Education,Job)


if __name__ == '__main__':
#Run the application
    main()
