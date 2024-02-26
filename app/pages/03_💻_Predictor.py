import streamlit as st
from service import predict

st.set_page_config(layout="centered")

st.header("Formulario para predecir transacciones fraudulentas")

with st.form("form_predict"):
    st.text_input("Monto", key="amount", placeholder="ejemplo 9000")
    st.text_input("Fecha", key="date", placeholder="ejemplo 2021-12-31")
    st.text_input("Hora", key="time", placeholder="ejemplo 12:00:00")
    st.selectbox("Tipo de transacción", ["Transferencia", "Cash-in"], key="type")
    st.selectbox("Horario", ["Mañana", "Tarde", "Noche"], key="schedule")
    submitted = st.form_submit_button("Predecir")

if submitted: 
    data = {
        "amount": st.session_state.amount,
        "date": st.session_state.date,
        "time": st.session_state.time,
        "type": st.session_state.type,
        "schedule": st.session_state.schedule,
    }
    prediction = predict(data)
    
    if prediction == "Fraude":
        st.error("Transacción fraudulenta",icon="🚨")
    else:
        st.success("Transacción segura",icon="✅")
