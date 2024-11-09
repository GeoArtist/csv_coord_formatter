import streamlit as st
from streamlit.delta_generator import DeltaGenerator

SEP_OPTIONS: dict[str, str] = {
    " ": "Space",
    ",": "Comma",
    ";": "Semicolon",
    "\t": "Tab",
}


def sep_input_render(st_obj: DeltaGenerator, key: str = "input_sep") -> None:
    st_obj.selectbox(
        "Separator",
        list(SEP_OPTIONS.keys()),
        index=0,
        key=key,
        format_func=lambda option: SEP_OPTIONS[option],
    )
