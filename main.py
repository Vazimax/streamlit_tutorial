import streamlit as sl
from datetime import *
import pandas as pd
import time as t
import datetime
import json

sl.markdown("""
    <style>
            .st-emotion-cache-czk5ss.e16jpq800
            {
                visibility: hidden;
            }
            .st-emotion-cache-1wbqy5l.e17vllj40
            {
                visibility: hidden;
            }
    </style>
""", unsafe_allow_html=True)


sl.title('TEEST')
sl.subheader('Bakr')
sl.text('Naaaaaaaah')

sl.markdown('---')
sl.markdown(" **Heyo** *Daddy* ")
sl.markdown("# Big Man")
sl.markdown("[LinkedIn](https://www.linkedin.com)")
sl.latex(r"\begin{pmatrix}a\\c\end{pmatrix}")
json = {'a':'777','b':'555'}
sl.json(json)
code = """
    print('Teeeeeest')
"""
sl.code(code)


sl.markdown('---')
sl.write("### This is H3")
# sl.metric(label='Speed', value='99ms⁻¹', delta='1.4ms⁻¹')

# table = pd.DataFrame({'Column 1': [99,88,11,99,98,100], 'Column 2': [99,88,11,99,98,100]})
# sl.table(table)
# sl.dataframe(table)

# sl.image('test.png',caption='Test')
# sl.audio('test.mp3')
# sl.video('test.mp4')


def change():
    print('tessst')

sl.checkbox('Test', value=True, on_change=change(), key="checker")
sl.radio('Your age:', options=(18,20,22))

def agreement():
    print('Agreed')

sl.button('Agree',on_click=agreement())
sl.selectbox('Your location:', options=('Morocco','China','Germany','USA','England','Switzerland'))
sl.multiselect('Your location:', options=('Morocco','China','Germany','USA','England','Switzerland'))


sl.title('Uploading')
sl.markdown('---')
file = sl.file_uploader('PDF',type=['pdf'],accept_multiple_files=True)
if file is None:
    sl.text('There is no file yet!')


sl.slider('Slider')
color = sl.select_slider(
    "Select a color of the rainbow",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
sl.write("My favorite color is", color) 

sl.text_input('Enter your fav color:',max_chars=20)
sl.text_area('Why do you like this color:',max_chars=1000)
sl.date_input('Your birthday:',datetime.date(2004, 6, 7))


def conv(value):
    m,s,mm = value.split(":")
    t_s = int(m)*60 + int(s) + int(mm)/1000
    return t_s

value = sl.time_input('Set timer', value=time(0,0,0))
if str(value) == '00:00:00':
    sl.text('Please set a timer')
else:
    s = conv(str(value)) / 100
    bar = sl.progress(0)
    progress_status = sl.empty()
    for i in range(100):    
        bar.progress(i+1)
        progress_status.write(str(i+1) + '%')
        t.sleep(s)