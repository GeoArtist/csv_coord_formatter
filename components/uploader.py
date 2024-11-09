import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit.runtime.uploaded_file_manager import UploadedFile

from components.gap import gap_render
from components.index_col_input import index_col_input_render
from components.sep_input import sep_input_render


def uploader_render() -> UploadedFile | None:
    # Header
    upload_container: DeltaGenerator = st.container(border=True)
    upload_container.subheader("Upload CSV file", divider=True)
    gap_render(st_obj=upload_container)

    # Uploader
    uploaded_file: UploadedFile | None = upload_container.file_uploader(
        "Upload CSV file", type=["csv", "txt"], key="uploaded_file"
    )
    gap_render(st_obj=upload_container)

    if uploaded_file:
        st.markdown(
            """
        <style>[data-testid=toastContainer] [data-testid=stMarkdownContainer] > p {
    font-size: 20px; font-style: normal; font-weight: 400;
    foreground-color: #00ff00; background-color: #00ff00;
}</style>
        """,
            unsafe_allow_html=True,
        )
        st.toast("File uploaded successfully", icon="✅")
    # Input Params Expander
    expander: DeltaGenerator = upload_container.expander(
        "Upload Config Parameters", expanded=False
    )
    cols: list[DeltaGenerator] = expander.columns(2)
    # Separator
    sep_input_render(st_obj=cols[0])
    # Index column
    index_col_input_render(st_obj=cols[1])

    return uploaded_file
