import pandas as pd
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from components.gap import gap_render
from components.msgs import error_render
from utils.errors import CSVFormatError


def df_converter(uploaded_file: UploadedFile) -> pd.DataFrame:
    """Try to convert the uploaded file to a DataFrame.

    Check valid of input data format
    Parameters
    ----------
    uploaded_file : UploadedFile

    Returns
    -------
    pd.DataFrame

    Raises
    ------
    CSVFormatError
    """
    try:
        df: pd.DataFrame = pd.read_csv(
            uploaded_file,
            header=None,
            sep=st.session_state["input_sep"],
            index_col=st.session_state["input_index_col"],
        )
        if len(df.columns) != 4:
            raise CSVFormatError

    except CSVFormatError as e:
        gap_render()
        error_render(e.html_message)
        df = pd.DataFrame()
    except Exception as e:
        st.write(e)
        df = pd.DataFrame()
    return df
