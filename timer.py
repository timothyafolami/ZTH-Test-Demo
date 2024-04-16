import streamlit as st
import time


from datetime import timedelta

from streamlit.components.v1 import html

@st.cache_data()
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


def app():
    add_clock()

# add_clock(timedelta(days=2))