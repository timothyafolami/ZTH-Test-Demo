import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (
                                                          LoginError,
                                    )


def app():
    
    # loading the image 
    st.image('zth pic-1.jpg',use_column_width=True)

    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )

    # Creating a login widget
    try:
        authenticator.login()
    except LoginError as e:
        st.error(e)


    if st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')
    elif st.session_state["authentication_status"] is True:
    # logout button
        authenticator.logout("Logout", "sidebar")

        st.markdown(f'### Welcome *{st.session_state["name"]}* to Data Assessment Programme')
        # writing user name in a file
        with open('user.txt', 'w') as f:
            f.write(st.session_state["name"])


if __name__ == "__main__":
    app()