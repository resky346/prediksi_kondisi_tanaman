import streamlit as st
import numpy as np
import joblib

# Load model yang telah disimpan
model = joblib.load('Analisis_kondisi_tanaman_models.sav')

# Judul aplikasi
st.title("Aplikasi Analisis Kondisi Tanaman")

# Formulir input pengguna
st.sidebar.header("Masukkan Parameter")
soil_moisture = st.sidebar.slider("Kelembapan Tanah (%)", 0, 100, 50)
ambient_temp = st.sidebar.slider("Suhu Atmosfer (°C)", 0, 50, 25)
soil_temp = st.sidebar.slider("Suhu Tanah (°C)", 0, 50, 25)
humidity = st.sidebar.slider("Kelembapan Udara (%)", 0, 100, 50)
light_intensity = st.sidebar.slider("Intensitas Cahaya (lux)", 0, 1000, 500)
soil_ph = st.sidebar.slider("pH Tanah", 0.0, 14.0, 7.0)
nitrogen_level = st.sidebar.slider("Kadar Nitrogen (mg/kg)", 0, 100, 50)
phosphorus_level = st.sidebar.slider("Kadar Fosfor (mg/kg)", 0, 100, 50)
potassium_level = st.sidebar.slider("Kadar Kalium (mg/kg)", 0, 100, 50)
chlorophyll_content = st.sidebar.slider("Kadar Klorofil (SPAD)", 0, 100, 50)
electrochemical_signal = st.sidebar.slider("Sinyal Elektrokimia", 0.0, 10.0, 1.0)

# Tombol prediksi
if st.sidebar.button("Prediksi"):
    # Buat input fitur menjadi array
    input_data = np.array([[soil_moisture, ambient_temp, soil_temp, humidity, light_intensity, 
                            soil_ph, nitrogen_level, phosphorus_level, potassium_level, 
                            chlorophyll_content, electrochemical_signal]])
    
    # Lakukan prediksi
    prediction = model.predict(input_data)
    
    # Hasil prediksi
    health_status = {0: "Low Stress", 1: "Moderate Stress", 2: "High Stress"}
    st.subheader(f"Kondisi Tanaman: {health_status[prediction[0]]}")
