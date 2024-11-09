import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from components.download_btn import download_btn_render
from components.gap import gap_render
from components.header_opt_input import header_opt_input_render
from components.output_filename_input import output_filename_input_render
from components.sep_input import sep_input_render


def download_section_render(df: pd.DataFrame) -> None:
    wrapper: DeltaGenerator = st.container(border=True)
    wrapper.subheader("Download CSV file", divider=True)
    cols: list[DeltaGenerator] = wrapper.columns(3)

    # Output Params
    sep_input_render(key="output_sep", st_obj=cols[0])
    header_opt_input_render(st_obj=cols[1])
    output_filename_input_render(st_obj=cols[2])

    gap_render(st_obj=cols[1])
    download_btn_render(df=df, st_obj=cols[1])
