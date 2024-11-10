import pandas as pd
import streamlit as st
from pandas import DataFrame
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.uploaded_file_manager import UploadedFile

from components.gap import gap_render
from components.index_col_input import index_col_input_render
from components.msgs import info_render
from components.sep_input import sep_input_render
from utils.df import df_converter


def uploader_render() -> pd.DataFrame:
    # Header
    upload_container: DeltaGenerator = st.container(border=True)
    upload_container.subheader("Upload CSV file", divider="blue")
    gap_render(st_obj=upload_container)

    # Uploader
    uploaded_file: UploadedFile | None = upload_container.file_uploader(
        "Upload CSV file", type=["csv", "txt"], key="uploaded_file"
    )
    if uploaded_file:
        df: DataFrame = df_converter(uploaded_file, upload_container)
    else:
        info_render(
            "File should contain 4 columns: [Nr, X, Y, H]",
            st_obj=upload_container,
        )
        df = pd.DataFrame()

    if not df.empty:
        st.toast("File uploaded successfully", icon="✅")

    # Input Params Expander
    gap_render(st_obj=upload_container)
    expander: DeltaGenerator = upload_container.expander(
        "Upload Config Parameters", expanded=False
    )
    cols: list[DeltaGenerator] = expander.columns(2)
    # Separator
    sep_input_render(st_obj=cols[0])
    # Index column
    index_col_input_render(st_obj=cols[1])

    return df
