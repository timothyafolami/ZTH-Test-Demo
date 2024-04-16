import streamlit as st

def display_question(question_num, question_text, options):
    st.subheader(f"Question {question_num}: {question_text}")
    user_answer = st.radio(f"Select an answer for Question {question_num}:", options, key=f"question_{question_num}")
    return user_answer

def calculate_score(answers):
    # Define the correct answers (any option can be chosen)
    correct_answers = ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C']
    score = 0
    for user_answer, correct_answer in zip(answers, correct_answers):
        if user_answer.strip()[0].upper() == correct_answer.strip():
            score += 1
    return score

def main():
    st.title("Quiz App")
    
    # Questions and options
    questions = [
        ("Which store had the highest total weekly sales across all weeks?", ["A) Store 1", "B) Store 2", "C) Store 3", "D) Store 4"]),
        ("During which week did Store 2 have the highest weekly sales?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("What was the total weekly sales for all stores combined in the week with the highest sales?", ["A) $10,000,000", "B) $15,000,000", "C) $20,000,000", "D) $25,000,000"]),
        ("Which store had the lowest total weekly sales across all weeks?", ["A) Store 1", "B) Store 2", "C) Store 3", "D) Store 4"]),
        ("During which holiday week did Store 3 have the highest weekly sales?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("What was the average temperature across all stores during non-holiday weeks?", ["A) 42.31°F", "B) 38.51°F", "C) 39.93°F", "D) 46.63°F"]),
        ("During which week did Store 3 have the lowest weekly sales?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("Which store had the highest average weekly sales?", ["A) Store 1", "B) Store 2", "C) Store 3", "D) Store 4"]),
        ("What was the overall unemployment rate across all stores?", ["A) 8.106%", "B) 2.572%", "C) 2.548%", "D) 2.514%"]),
        ("During which week did the CPI reach its highest value?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("In which holiday week did Store 4 experience the lowest weekly sales?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("What was the percentage increase in weekly sales for Store 2 from the previous week with holiday to the following week without holiday?", ["A) 10%", "B) 15%", "C) 20%", "D) 25%"]),
        ("During which holiday week did Store 1 experience the highest weekly sales increase compared to the previous non-holiday week?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
        ("What was the average CPI across all stores during holiday weeks?", ["A) 211.096358", "B) 211.242170", "C) 211.289143", "D) 211.319643"]),
        ("During which non-holiday week did Store 3 experience the highest weekly sales compared to all other non-holiday weeks?", ["A) 2010-05-02", "B) 2010-12-02", "C) 2010-02-19", "D) 2010-02-26"]),
    ]

    # Display questions and collect answers
    user_answers = []
    for i, (question, options) in enumerate(questions, 1):
        user_answer = display_question(i, question, options)
        user_answers.append(user_answer)
    
    # adding a submit button
    if st.button("Submit"):
        
        total_score = calculate_score(user_answers)
        # Display total score
        st.write(f"Your total score is: {total_score}/{len(questions)}")

if __name__ == "__main__":
    main()
