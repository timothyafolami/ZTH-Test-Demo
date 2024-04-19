import streamlit as st
import pandas as pd
from st_supabase_connection import SupabaseConnection
from utils import calculate_cosine_similarity
import os


# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# This is an autograder page. 

def grade_assessment():
    # getting the user data
    user_data = pd.read_csv("user_responses.csv")

    # getting the respective cols
    generated_answer = user_data.iloc[0].tolist()[1:]

    # making inference with the grading function
    user_grade = calculate_cosine_similarity(generated_answer)

    # getting the user name from the file
    with open('user.txt', 'r') as f:
        user_name = f.read()
    # recording the username and grade in the database
    conn.table("assessment_grades").insert({"user_name": user_name, "grade": user_grade*100}).execute()

    try:
        os.remove("user.txt")
        os.remove("user_responses.csv")
    except FileNotFoundError:
        pass
    # returning the grade
    return user_grade

def app():
    st.title("Welcome to the Autograder Page")
    st.markdown("#### Here your assessment is graded. No worries, just chill.")
    st.write("Click the button below to grade your assessment.")

    # Button to trigger grading action
    if st.button("Grade"):
        # adding some animations
        with st.spinner("Grading..."):
            # use try and except to handle the case where the file is not found
            try:
                st.write("Grading your assessment...")
                grade_result = grade_assessment() * 100
                # a quick animation
                st.balloons()
                st.write("Grading completed!")
                st.markdown(f"### {grade_result}")
                # Delete user.txt and user_responses.csv
                
            except FileNotFoundError:
                st.error("Please complete the assessment first.")

if __name__ == "__main__":
    app()