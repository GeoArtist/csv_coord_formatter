import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def processing_params_render() -> None:
    # Processing Params Expander
    exp: DeltaGenerator = st.expander(
        "Processing Config Parameters", expanded=True
    )
    cols: list[DeltaGenerator] = exp.columns(2)
    cols[0].number_input(
        "X,Y decimal places", value=2, key="x_y_round", min_value=0
    )
    cols[1].number_input("H decimal place", value=1, key="h_round", min_value=0)
