import pandas as pd
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile

from components.css import css_render
from components.data_viewer import data_viewer_render
from components.download_section import download_section_render
from components.gap import gap_render
from components.processing_params import processing_params_render
from components.uploader import uploader_render
from utils.data_process import process

st.set_page_config(page_title="CSV Coordinate Formatter")

css_render("h2, h3 {width:fit-content; margin-inline:auto;}")

st.header("CSV COORDINATE FORMATTER")
gap_render()
# Uploader render
uploaded_file: UploadedFile | None = uploader_render()

# Processing Params render
processing_params_render()

if uploaded_file:
    df: pd.DataFrame = process(uploaded_file)

    data_viewer_render(df)
    download_section_render(df)
