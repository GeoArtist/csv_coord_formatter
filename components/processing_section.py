import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from components.data_viewer import data_viewer_render
from components.gap import gap_render
from utils.data_process import process


def processing_section_render(input_df: pd.DataFrame) -> pd.DataFrame:

    # Processing Params Expander
    wrapper: DeltaGenerator = st.container(border=True)
    # Subheader
    wrapper.subheader("Processing settings", divider="green")
    gap_render(st_obj=wrapper)

    # Setting inputs
    cols: list[DeltaGenerator] = wrapper.columns(2)
    cols[0].number_input(
        "X,Y decimal places", value=2, key="x_y_round", min_value=0
    )
    cols[1].number_input("H decimal place", value=1, key="h_round", min_value=0)

    # Process data
    df: pd.DataFrame = process(input_df)

    # Data Viewer
    data_viewer_render(df, st_obj=wrapper)
    return df
