import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def download_btn_render(df: pd.DataFrame, st_obj: DeltaGenerator) -> None:

    csv: str = df.to_csv(
        index=True,
        encoding="utf-8",
        header=st.session_state["header_opt_input"],
        sep=st.session_state["output_sep"],
    )

    file_name: str = st.session_state["output_filename_input"]

    st_obj.download_button(
        "Download CSV",
        data=csv,
        file_name=f"{file_name}.csv",
        mime="text/csv",
        key="download_csv_btn",
        type="primary",
        use_container_width=True,
    )
