import streamlit as st

# Fungsi untuk menentukan klasifikasi berdasarkan input pengguna
def classify_pellet(moisture, ash, durability, fines, trace_element, net_calorific_value, density, 
                     nitrogen, sulphur, chlorine, arsenic, cadmium, chromium, copper, lead, mercury, nickel, zinc):

    # Kriteria untuk setiap kelas
    criteria = {
        "I1": {
            "moisture": 10, "ash": 1.5, "durability": 97.5, "fines": 4.0, "trace_element": 3,
            "net_calorific_value": 16.5, "density": 600, "nitrogen": 0.5, "sulphur": 0.05, "chlorine": 0.03,
            "arsenic": 1, "cadmium": 1.5, "chromium": 10, "copper": 10, "lead": 10, "mercury": 0.1,
            "nickel": 10, "zinc": 100
        },
        "I2": {
            "moisture": 10, "ash": 3.0, "durability": 96.5, "fines": 5.0, "trace_element": 3,
            "net_calorific_value": 16.5, "density": 550, "nitrogen": 0.7, "sulphur": 0.05, "chlorine": 0.05,
            "arsenic": 1, "cadmium": 1.5, "chromium": 10, "copper": 10, "lead": 10, "mercury": 0.1,
            "nickel": 10, "zinc": 100
        },
        "I3": {
            "moisture": 10, "ash": 5.0, "durability": 95.0, "fines": 6.0, "trace_element": 3,
            "net_calorific_value": 16.5, "density": 500, "nitrogen": 0.7, "sulphur": 0.05, "chlorine": 0.1,
            "arsenic": 1, "cadmium": 1.5, "chromium": 10, "copper": 10, "lead": 10, "mercury": 0.1,
            "nickel": 10, "zinc": 100
        }
    }

    # Cek kriteria dari I1 ke I3
    for grade in ["I1", "I2", "I3"]:
        c = criteria[grade]
        if (moisture <= c["moisture"] and ash <= c["ash"] and durability >= c["durability"] and
            fines <= c["fines"] and trace_element <= c["trace_element"] and net_calorific_value >= c["net_calorific_value"] and
            density >= c["density"] and nitrogen <= c["nitrogen"] and sulphur <= c["sulphur"] and chlorine <= c["chlorine"] and
            arsenic <= c["arsenic"] and cadmium <= c["cadmium"] and chromium <= c["chromium"] and copper <= c["copper"] and
            lead <= c["lead"] and mercury <= c["mercury"] and nickel <= c["nickel"] and zinc <= c["zinc"]):
            return grade
    
    return "Tidak memenuhi standar I1, I2, atau I3"

# UI Streamlit
# UI Streamlit
st.markdown("<h1 style='text-align: center;'>Klasifikasi Kualitas Wood Pellet</h1>", unsafe_allow_html=True)


# Input pengguna
moisture = st.number_input("Total Moisture (%)", min_value=0.0, max_value=100.0, step=0.1)
ash = st.number_input("Ash (%)", min_value=0.0, max_value=100.0, step=0.1)
durability = st.number_input("Durability (%)", min_value=0.0, max_value=100.0, step=0.1)
fines = st.number_input("Fines (%)", min_value=0.0, max_value=100.0, step=0.1)
trace_element = st.number_input("Trace Element (mg/kg)", min_value=0.0, max_value=100.0, step=0.1)
net_calorific_value = st.number_input("Net Calorific Value (MJ/kg)", min_value=0.0, max_value=100.0, step=0.1)
density = st.number_input("Density (kg/m³)", min_value=0.0, max_value=1000.0, step=0.1)
nitrogen = st.number_input("Nitrogen (%)", min_value=0.0, max_value=10.0, step=0.01)
sulphur = st.number_input("Sulphur (%)", min_value=0.0, max_value=10.0, step=0.01)
chlorine = st.number_input("Chlorine (mg/kg)", min_value=0.0, max_value=10.0, step=0.01)
arsenic = st.number_input("Arsenic (mg/kg)", min_value=0.0, max_value=10.0, step=0.01)
cadmium = st.number_input("Cadmium (mg/kg)", min_value=0.0, max_value=10.0, step=0.01)
chromium = st.number_input("Chromium (mg/kg)", min_value=0.0, max_value=100.0, step=0.1)
copper = st.number_input("Copper (mg/kg)", min_value=0.0, max_value=100.0, step=0.1)
lead = st.number_input("Lead (mg/kg)", min_value=0.0, max_value=100.0, step=0.1)
mercury = st.number_input("Mercury (mg/kg)", min_value=0.0, max_value=10.0, step=0.01)
nickel = st.number_input("Nickel (mg/kg)", min_value=0.0, max_value=100.0, step=0.1)
zinc = st.number_input("Zinc (mg/kg)", min_value=0.0, max_value=1000.0, step=1.0)

# Tombol klasifikasi
if st.button("Klasifikasikan"):
    result = classify_pellet(moisture, ash, durability, fines, trace_element, net_calorific_value, density, 
                             nitrogen, sulphur, chlorine, arsenic, cadmium, chromium, copper, lead, mercury, nickel, zinc)
    st.write(f"*Hasil Klasifikasi:* {result}")

