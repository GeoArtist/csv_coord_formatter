import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def gap_render(
    row_number: int = 1,
    st_obj: DeltaGenerator = st,
) -> None:
    st_obj.markdown(f"""{row_number * '<br>'}""", unsafe_allow_html=True)
