import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# # Perform query.
# rows = conn.query("*", table="user_responses", ttl="10m").execute()

# # Print results.
# for row in rows.data:
#     st.write(row)

# Define the new user's data.
new_user_data = {
    "user_name": "Olawale",
    "excel_question_1": "Some answer for Excel Question 1",
    "excel_question_2": "Some answer for Excel Question 2",
    "excel_question_3": "Some answer for Excel Question 3",
    "excel_question_4": "Some answer for Excel Question 4",
    "excel_question_5": "Some answer for Excel Question 5",
    "excel_question_6": "Some answer for Excel Question 6",
    "excel_question_7": "Some answer for Excel Question 7",
    "excel_question_8": "Some answer for Excel Question 8",
    "excel_question_9": "Some answer for Excel Question 9",
    "excel_question_10": "Some answer for Excel Question 10",
    "excel_question_11": "Some answer for Excel Question 11",
    "excel_question_12": "Some answer for Excel Question 12",
    "excel_question_13": "Some answer for Excel Question 13",
    "excel_question_14": "Some answer for Excel Question 14",
    "excel_question_15": "Some answer for Excel Question 15",
    "excel_question_16": "Some answer for Excel Question 16",
    "excel_question_17": "Some answer for Excel Question 17",
    "sql_question_1": "Some answer for SQL Question 1",
    "sql_question_2": "Some answer for SQL Question 2",
    "sql_question_3": "Some answer for SQL Question 3",
    "sql_question_4": "Some answer for SQL Question 4",
    "sql_question_5": "Some answer for SQL Question 5",
    "sql_question_6": "Some answer for SQL Question 6",
    "sql_question_7": "Some answer for SQL Question 7",
    "sql_question_8": "Some answer for SQL Question 8",
    "sql_question_9": "Some answer for SQL Question 9",
    "sql_question_10": "Some answer for SQL Question 10",
    "sql_question_11": "Some answer for SQL Question 11",
    "power_bi_question_1": "Some answer for Power BI Question 1",
    "power_bi_question_2": "Some answer for Power BI Question 2",
    "power_bi_question_3": "Some answer for Power BI Question 3",
    "power_bi_question_4": "Some answer for Power BI Question 4",
    "power_bi_question_5": "Some answer for Power BI Question 5",
    "power_bi_question_6": "Some answer for Power BI Question 6",
    "power_bi_question_7": "Some answer for Power BI Question 7",
    "power_bi_question_8": "Some answer for Power BI Question 8"
}
# Insert the new row into the table.
conn.table("user_responses").insert(new_user_data).execute()

# Print a success message.
st.success("New user data added successfully!")