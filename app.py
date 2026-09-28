import streamlit as st
import pandas as pd
from streamlit.column_config import TextColumn

st.header("Calculadora para liquidaciones")

intro = """\
En la tabla puedes poner los números que quieras sumar. Abajo aparecerá el total, que se actualizará automáticamente.
- Puedes incluir multiplicaciones con asterisco * y divisiones con slash / en la tabla
- Puedes usar la columna de "Interruptores" para quitar o dejar los números de la suma sin necesidad de borrarlos
- Puedes usar el selector de filas a la izquierda para borrar filas (o resetear la tabla completamente)
"""
ocultar = st.checkbox('focus mode',value=False)

if not ocultar:
    st.markdown(intro)

def calcular_total(df):
    """Versión que toma la tabla en vez de texto"""
    expresiones_encendidas = df.loc[df['Interruptores']==True]['Números']
    resultado = sum([eval(e.strip()) for e in expresiones_encendidas])
    return resultado

data_df = pd.DataFrame(
    {
        "Interruptores": [True, True, True, False],
        "Números": [
            "1000",
            "2000 / 5",
            "50 * 15",
            "1234",
        ],
    }
)

edited_data = st.data_editor(
    data = data_df,
    width='content',
    height='content',
    column_config={
        "Interruptores": st.column_config.CheckboxColumn(
            "Interruptores",
            help="Considera o no este número en el total",
            default=True,
        ),
        "Números" : st.column_config.TextColumn(
            "Números",
            help= "Puedes incluir multiplicaciones con * y divisiones con /"
        )
    },
    #disabled=["Números"],
    hide_index=True,
    key='data',
    num_rows='dynamic'
)

total = calcular_total(edited_data)
st.markdown(f"**Total**: ``{total}``")
