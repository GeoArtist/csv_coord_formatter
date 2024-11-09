import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def data_viewer_render(df: pd.DataFrame) -> None:
    cols: list[DeltaGenerator] = st.columns([0.5, 1, 0.5])
    cols[1].dataframe(df, use_container_width=True, height=200)
