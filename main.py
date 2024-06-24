import streamlit as sl
import json


sl.title('TEEST')
sl.subheader('Bakr')
sl.text('Naaaaaaaah')

sl.markdown(" **Heyo** *Daddy* ")
sl.markdown("# Big Man")
sl.markdown("[LinkedIn](https://www.linkedin.com)")
sl.markdown('---')
sl.latex(r"\begin{pmatrix}a\\c\end{pmatrix}")
json = {'a':'777','b':'555'}
sl.json(json)
code = """
    print('Teeeeeest')
"""
sl.code(code)
