import pandas as pd
import streamlit as st

from components.css import css_render
from components.download_section import download_section_render
from components.gap import gap_render
from components.processing_section import processing_section_render
from components.uploader import uploader_render

st.set_page_config(
    page_title="CSV Coordinate Formatter", page_icon="favicon.ico"
)
st.session_state["app_error"] = None
css_render("h2, h3 {width:fit-content; margin-inline:auto;}")

st.header("CSV COORDINATE FORMATTER")
gap_render()

# Uploader render
uploaded_df: pd.DataFrame = uploader_render()


if not uploaded_df.empty:
    # Processing Section
    df: pd.DataFrame = processing_section_render(uploaded_df)
    # Download Section
    download_section_render(df)
