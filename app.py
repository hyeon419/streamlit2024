import streamlit as st
import random as r

st.header('주사위 게임', divider='rainbow')
clicked = st.button('주사위던지기', type='primary')

if clicked :
    n = r.randint(1,6)
    st.image(f'./img/{n}.png')