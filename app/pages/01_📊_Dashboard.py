import streamlit as st
import streamlit.components as components
from tableau import html_tableau
st.title("Dashboard de transacciones fraudulentas", anchor=False)
# components.html("""<iframe title="DashboardNC" width="800" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiNDI5MTdkNjMtN2NlMC00YzEzLTk1NjYtMjNhNTQwMTAzYmJhIiwidCI6ImZiNDMzYzc2LWJjNTktNGQ5OS04N2RmLWQ2OWJmZThmZDhiMCIsImMiOjR9&pageName=ReportSection464e96274072c40c4ee0" frameborder="0" allowFullScreen="true"></iframe>""")


st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiNDI5MTdkNjMtN2NlMC00YzEzLTk1NjYtMjNhNTQwMTAzYmJhIiwidCI6ImZiNDMzYzc2LWJjNTktNGQ5OS04N2RmLWQ2OWJmZThmZDhiMCIsImMiOjR9&pageName=ReportSection464e96274072c40c4ee0", width=900, height=600, scrolling=True)

