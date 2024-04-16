import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

def display_excel_questions(session_state):
    if "excel_answers" not in session_state:
        session_state["excel_answers"] = [""] * 17
    st.subheader("Excel Assessment")
    st.write("Please answer the following Excel-related questions:")
    excel_questions = [
        "What is Excel used for?",
        "Explain the difference between a workbook and a worksheet.",
        "Explain the VLOOKUP function.",
        "What is the CONCATENATE function used for?",
        "How can you remove duplicates in Excel?",
        "Explain how the PivotTable works and mention some of its functions.",
        "How is HLOOKUP different from VLOOKUP?",
        "How do you find and replace data in Excel?",
        "Explain the difference between COUNT, COUNTA, COUNTIF, and COUNTIFS functions.",
        "What is conditional formatting, and how do you apply it?",
        "What is the use of Comparative operators, logical tests and IF statements?",
        "How can you round the values if a whole column to 2 decimal places?",
        "Explain the difference between relative and absolute cell references?",
        "What is the difference between line chart and scatterplot? What are they used for?",
        "What is the purpose of the TRIM function?",
        "How can you link data between different worksheets?",
        "Explain the difference between the terms ‘filter’ and ‘sort’ in Excel."
    ]
    for i, question in enumerate(excel_questions, 1):
        st.write(f"**Question {i}:** {question}")
        session_state["excel_answers"][i-1] = st.text_area(f"Answer to Excel Question {i}", session_state["excel_answers"][i-1], key=f"excel_{i}")
    return session_state["excel_answers"]

def display_sql_questions(session_state):
    if "sql_answers" not in session_state:
        session_state["sql_answers"] = [""] * 11
    st.subheader("SQL Assessment")
    st.write("Please answer the following SQL-related questions:")
    sql_questions = [
        "What is SQL?",
        "What is an SQL statement? Give some examples.",
        "What is a database? What is DBMS, and what types of DBMS do you know? What is RDBMS? Give some examples of RDBMS.",
        "What is a join? What types of joins do you know? Explain their usage.",
        "What is a primary key? What is a unique key? What is a foreign key?",
        "What is a schema?",
        "What is the CASE() function?",
        "Briefly explain the purpose of the following functions: SELECT – FROM – JOIN – ON – WHERE – GROUP BY – HAVING – ORDER BY – LIMIT",
        "What are the possible values of a BOOLEAN data field?",
        "How to prevent duplicate records when making a query?",
        "What is the difference between renaming a column and giving an alias to it?"
    ]
    for i, question in enumerate(sql_questions, 1):
        st.write(f"**Question {i}:** {question}")
        session_state["sql_answers"][i-1] = st.text_area(f"Answer to SQL Question {i}", session_state["sql_answers"][i-1], key=f"sql_{i}")
    return session_state["sql_answers"]

def display_power_bi_questions(session_state):
    if "power_bi_answers" not in session_state:
        session_state["power_bi_answers"] = [""] * 8
    st.subheader("Power BI Assessment")
    st.write("Please answer the following Power BI-related questions:")
    power_bi_questions = [
        "What is Power BI?",
        "Difference between Power Query and Power Pivot",
        "What is Power BI Desktop",
        "What is Power Pivot?",
        "What is Power Query?",
        "What is DAX?",
        "What are Filters in Power BI?",
        "What is GetData in Power BI?"
    ]
    for i, question in enumerate(power_bi_questions, 1):
        st.write(f"**Question {i}:** {question}")
        session_state["power_bi_answers"][i-1] = st.text_area(f"Answer to Power BI Question {i}", session_state["power_bi_answers"][i-1], key=f"power_bi_{i}")
    return session_state["power_bi_answers"]

def main():
    session_state = st.session_state

    st.title("Data Assessment Programme")

    mast_df = conn.read(spreadsheet=st.secrets['spreadsheet'])

    # Introduction
    st.write("Welcome to the Data Assessment Programme. This program will test your knowledge in Excel, SQL, and Power BI")

    # Get user name
    user_name = st.text_input("Enter your name")

    # Display Excel questions
    excel_answers = display_excel_questions(session_state)

    # Display SQL questions
    sql_answers = display_sql_questions(session_state)

    # Display Power BI questions
    power_bi_answers = display_power_bi_questions(session_state)

    # Submission
    if st.button("Submit Answers"):
        # Validate if user name is provided
        if not user_name:
            st.error("Please enter your name.")
        else:
            # Validate if all text areas are filled
            if all(excel_answers) and all(sql_answers) and all(power_bi_answers):
                # Combine answers into a dataframe
                data = {
                    "User Name": [user_name],
                    **{f"Excel Question {i}": [answer] for i, answer in enumerate(excel_answers, 1)},
                    **{f"SQL Question {i}": [answer] for i, answer in enumerate(sql_answers, 1)},
                    **{f"Power BI Question {i}": [answer] for i, answer in enumerate(power_bi_answers, 1)}
                }
                df = pd.DataFrame(data)
                st.write("Thank you for submitting your answers!")
                # Save the user responses to the master dataframe
                # Append the data to a file, database, or Google Sheets
                update_df = pd.concat([mast_df, df], ignore_index=True, axis=0)

                # Write the updated dataframe to Google Sheets
                conn.write(spreadsheet=st.secrets['spreadsheet'], data=update_df, sheet_name="Sheet1")
            else:
                st.error("Please answer all questions before submitting.")

if __name__ == "__main__":
    main()
