import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# g_sheet = st.secrets['spreadsheet']

df = conn.read(spreadsheet=st.secrets['spreadsheet'])

df_1 = pd.read_csv("t11.csv")


# Print results.
st.dataframe(df)
updated_df = pd.concat([df, df_1], ignore_index=True, axis=0)
st.dataframe(updated_df)

# Write the updated dataframe to Google Sheets
conn.update(spreadsheet=st.secrets['spreadsheet'], data=updated_df, worksheet="Sheet1")
# st.write("Data has been written to Google Sheets")