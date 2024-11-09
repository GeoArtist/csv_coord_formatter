import streamlit as st
from streamlit.delta_generator import DeltaGenerator

HEADER_OPT: dict[bool, str] = {
    True: "Yes",
    False: "No",
}


def header_opt_input_render(
    st_obj: DeltaGenerator, key: str = "header_opt_input"
) -> None:

    st_obj.selectbox(
        "Add header",
        options=list(HEADER_OPT.keys()),
        index=1,
        key=key,
        format_func=lambda option: HEADER_OPT[option],
    )
