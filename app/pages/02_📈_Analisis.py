import streamlit as st

st.header("Análisis de datos de transacciones fraudulentas")

st.markdown("""
### El objetivo
- Predecir si una transacción es fraudulenta o no.
- Brindar un servicio de predicción de transacciones fraudulentas.
### El modelo
- Se utilizó un modelo de Machine Learning llamado Gradient Boosting.
- El modelo de predicción de transacciones fraudulentas tiene una precisión del 98%.
- Hay que tener en cuenta que el modelo no es perfecto y puede haber falsos positivos.
- Las variables más importantes para la predicción son el monto de la transacción, el saldo anterior del destino y el tipo de transacción.
### El servicio
- Se creó un servicio web que recibe
    - El paso de la transacción.
    - El monto de la transacción.
    - El saldo anterior del origen.
    - El saldo anterior del destino
    - El tipo de transacción.
    - El horario de la transacción.
    - Si la transacción se realizó en fin de semana.
- El servicio devuelve si la transacción es fraudulenta o no.


""")