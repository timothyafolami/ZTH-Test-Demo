import streamlit as st

## Creating a Welcome Page for the Users


def app():
    st.title("Welcome to Zion Tech Hub!")
    st.markdown("## We are glad to have you onboard.")
    st.markdown("---")
    st.markdown("## About the Assessment:")
    st.markdown("This is an assessment for our Intermediate Data Analyst program. We have some questions we want to use to test your knowledge to see if you have the necessary understanding to be in the intermediate class. Please note that this assessment is for your benefit, to ensure you have the best learning experience.")
    st.markdown("### This Assessment covers three main aspects of data analytics: EXCEL, SQL, and POWER BI.")
    st.markdown("### The assessment duration is 30 minutes. Make sure to answer the questions within the allotted time.")
    st.markdown("---")
    st.markdown("## How to Proceed:")
    st.markdown("1. Go to the login page and log in to participate. Your first name is your username, and your last name is your password. Remember, the first letters are capitalized.")
    st.markdown("2. Once logged in, click on 'Assessment' to get started.")
    st.markdown("3. Answer the questions in the assessment.")
    st.markdown("4. Click on 'Submit Answers' to submit your responses.")
    st.markdown("5. After submitting your answers, Go to the 'Autograder' page to check your grade.")
    st.markdown("---")
    st.markdown("## Best of Luck!")

if __name__ == "__main__":
    app()