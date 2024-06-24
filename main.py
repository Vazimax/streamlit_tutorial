import streamlit as sl
import pandas as pd
import json


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
sl.metric(label='Speed', value='99ms⁻¹', delta='1.4ms⁻¹')

table = pd.DataFrame({'Column 1': [99,88,11,99,98,100], 'Column 2': [99,88,11,99,98,100]})
sl.table(table)
sl.dataframe(table)