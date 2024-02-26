import streamlit as st

with st.form("form_predict"):
    st.text_input("Monto", key="amount",placeholder="ejemplo 9000")
    st.text_input("Fecha", key="date",placeholder="ejemplo 2021-12-31")
    st.text_input("Hora", key="time",placeholder="ejemplo 12:00:00")
    st.selectbox("Tipo de transacción", ["Transferencia", "Cash-in"], key="type")
    st.form_submit_button("Predecir")