import streamlit as st
from service import predict

st.set_page_config(layout="centered")

st.header("Formulario para predecir transacciones fraudulentas")

with st.form("form_predict"):
    st.write("Por favor, ingrese los datos de la transacción")
    step = st.number_input("Step",min_value=0)
    monto = st.number_input("Monto",min_value=0)
    oldbalanceOrg = st.number_input("OldbalanceOrg",min_value=0)
    oldbalanceDest = st.number_input("OldbalanceDest",min_value=0)
    type_transfer = st.selectbox("Tipo de transacción",["CASH_OUT","TRANSFER"])
    horario = st.selectbox("Horario",["Mañana","Tarde","Noche"])
    fin_de_semana = st.checkbox("¿La transacción se realizó en fin de semana?")
    submitted = st.form_submit_button("Predecir")
    
if submitted: 
    data = {
        "step": step,
        "monto": monto,
        "oldbalanceOrg": oldbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "type_CASH_OUT": 0,
        "type_TRANSFER": 0,
        "fin_de_semana": fin_de_semana,
        "mañana": 0,
        "noche": 0,
        "tarde": 0
    }
    data[f"type_{type_transfer}"] = 1
    data[f"{horario.lower()}"] = 1
    prediction = predict(data)
    
    if prediction:
        st.error("Transacción fraudulenta",icon="🚨")
    else:
        st.success("Transacción segura",icon="✅")
    # st.write(data)
    
    
