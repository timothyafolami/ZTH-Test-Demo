import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# g_sheet = st.secrets['spreadsheet']

df = conn.read(spreadsheet=st.secrets['spreadsheet'])

# Print results.
st.dataframe(df)
st.write(df.columns.tolist())
st.write(type(df))