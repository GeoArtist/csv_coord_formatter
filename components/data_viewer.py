import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def data_viewer_render(df: pd.DataFrame, st_obj: DeltaGenerator) -> None:
    cols: list[DeltaGenerator] = st_obj.columns([0.5, 1, 0.5])
    cols[1].dataframe(df, use_container_width=True, height=200)
