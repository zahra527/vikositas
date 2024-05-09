import streamlit as st

st.header('Aplikasi Penetapan Kekentalan Metode Laju Alir Oswald/Engler', divider='rainbow')

densitas_sampel = st.number_input('masukan densitas sampel')
st.write('the first number is',densitas_sampel)

X̅laju_alir_sampel= st.number_input ('masukkan X̅laju alir sampel')
st.write('the second number is',X̅laju_alir_sampel)

densitas_air = st.number_input ('masukan densitas air')
st.write('the second number is',densitas_air)

X̅laju_alir_air= st.number_input('masukkan X̅laju alir air')
st.write('the second number is',X̅laju_alir_air)

viskositas_aquadest= st.number_input('masukkan viskositas aquadest')
st.write('the second number is',viskositas_aquadest)

viskositas= (densitas_sampel * X̅laju_alir_sampel) / (densitas_air * X̅laju_alir_air) * viskositas_aquadest
st.write(f" {densitas_sampel} x  {X̅laju_alir_sampel} ÷ {densitas_air} x {X̅laju_alir_air} x {viskositas_aquadest}={viskositas}")