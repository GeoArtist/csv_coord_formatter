import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def output_filename_input_render(
    st_obj: DeltaGenerator, key: str = "output_filename_input"
) -> None:
    file_name: str = (
        st.session_state["uploaded_file"].name.split(".")[0] + "_formatted"
    )
    st_obj.text_input("Outputfilename", key=key, value=file_name)
