import streamlit as st
import time
from datetime import timedelta
from streamlit.components.v1 import html

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

def add_clock(length: timedelta = timedelta(hours=1)):
    st.markdown('## Timer')
    num_seconds = length.total_seconds()
    html(
        """
        <h1>Countdown Clock</h1>
    <div id="clockdiv">
    <div>
        <span class="hours"></span>
        <div class="smalltext">Hours</div>
    </div>
    <div>
        <span class="minutes"></span>
        <div class="smalltext">Minutes</div>
    </div>
    <div>
        <span class="seconds"></span>
        <div class="smalltext">Seconds</div>
    </div>
    <div id="start">Start</div>
    </div>
    <script>
    function getTimeRemaining(endtime) {
    const total = Date.parse(endtime) - Date.parse(new Date());
    const seconds = Math.floor((total / 1000) % 60);
    const minutes = Math.floor((total / 1000 / 60) % 60);
    const hours = Math.floor((total / (1000 * 60 * 60)) % 24);

    return {
        total,
        hours,
        minutes,
        seconds
    };
    }

    function initializeClock(id, endtime) {
    const clock = document.getElementById(id);
    const hoursSpan = clock.querySelector('.hours');
    const minutesSpan = clock.querySelector('.minutes');
    const secondsSpan = clock.querySelector('.seconds');

    function updateClock() {
        const t = getTimeRemaining(endtime);

        hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
        minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
        secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

        if (t.total <= 0) {
        clearInterval(timeinterval);
        }
    }

    updateClock();
    document.getElementById('start').addEventListener('click', function() {
        const timeinterval = setInterval(updateClock, 1000);
    })
    }
    """
        + f"const deadline = new Date(Date.parse(new Date()) + {num_seconds} * 1000);"
        + """
    initializeClock('clockdiv', deadline);
    </script>
    <style>
    body{
    text-align: center;
    background: #00ECB9;
    font-family: sans-serif;
    font-weight: 100;
    }

    h1{
    color: #396;
    font-weight: 100;
    font-size: 40px;
    margin: 40px 0px 20px;
    }

    #clockdiv{
    position: fixed;
    font-family: sans-serif;
    color: #fff;
    display: inline-block;
    font-weight: 100;
    text-align: center;
    font-size: 30px;
    }

    #clockdiv > div{
    padding: 10px;
    border-radius: 3px;
    background: #00BF96;
    display: inline-block;
    }

    #clockdiv div > span{
    padding: 15px;
    border-radius: 3px;
    background: #00816A;
    display: inline-block;
    }

    .smalltext{
    padding-top: 5px;
    font-size: 16px;
    }

    #start{
    display: block !important;
    margin-top: 10px;
    cursor: pointer;
    }
    </style>
    """,
        height=300,
    )

def main():
    add_clock()
    st.title("Welcome to the Quiz App")

    # Welcome message and start button
    st.write("This is a timed quiz. You will have one hour to complete it.")
    if st.button("Start"):
        start_time = time.time()
        remaining_time = 3600  # 1 hour in seconds
        while remaining_time > 0:
            # Calculate remaining time
            elapsed_time = time.time() - start_time
            remaining_time = max(0, 3600 - elapsed_time)  # Ensure remaining time doesn't go negative
            minutes = int(remaining_time // 60)
            seconds = int(remaining_time % 60)
            
            # Display timer
            st.markdown(f"**Time Remaining:** {minutes:02d}:{seconds:02d}")
            st.write("---")
            
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
                
            if remaining_time == 0:
                end_time = time.time()
                elapsed_time = end_time - start_time
                total_score = calculate_score(user_answers)
                st.write(f"Your total score is: {total_score}/{len(questions)}")
                st.write(f"Time taken: {int(elapsed_time // 60)} minutes {int(elapsed_time % 60)} seconds")
                break
            time.sleep(1)

if __name__ == "__main__":
    main()
