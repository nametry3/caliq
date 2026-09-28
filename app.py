from cProfile import label

import streamlit as st

st.header("Calculadora simple para liquidaciones")
st.subheader("Por ahora solo es eso...")

def calc(text:str) -> str:
    """Calcula lo indicado por el texto; suma el resultado de cada línea"""
    try:
        return str(eval(text.strip().replace('\n','+').strip()))
    except SyntaxError as s:
        return "SyntaxError :S"


texto = st.text_area(
    label='Pon los números aquí, uno en cada línea. Puedes poner multiplicaciones y divisiones'
    ,height='content'
    ,value = """1000
100 * 3
10 / 5
-1"""
)

st.write(f"Total: ``{calc(texto)}``")
