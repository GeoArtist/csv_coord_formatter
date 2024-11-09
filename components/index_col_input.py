import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def index_col_input_render(
    st_obj: DeltaGenerator, key: str = "input_index_col"
) -> None:
    st_obj.number_input("Index column", value=0, key=key, min_value=0)
