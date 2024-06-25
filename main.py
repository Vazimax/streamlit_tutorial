import streamlit as sl
import pandas as pd
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