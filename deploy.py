import pandas as pd
import streamlit as st
import joblib

x_numericos = {'Pregnancies': 0, 'Glucose': 0, 'BloodPressure': 0, 'SkinThickness': 0, 'Insulin': 0, 'BMI': 0, 'Age': 0,}
dicionario = {}

for item in x_numericos:
    if item == 'BMI':
        valor = st.number_input(f'{item}', step=0.1, value=0.0, format="%.1f")
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor

botao = st.button('Você tem diabetes?')

if botao:
    dicionario.update(x_numericos)
    valores_x = pd.DataFrame(dicionario, index=[0])
    modelo = joblib.load('modelo.joblib')
    preco = modelo.predict(valores_x)
    if preco[0] == 1:
        st.write('Tem diabetes')
    else:
        st.write('Não tem diabetes')
