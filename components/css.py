import streamlit as st


def css_render(css: str = "", html: str = "") -> None:

    st.markdown(
        f"""
                <style>{css}</style>
                {html}""",
        unsafe_allow_html=True,
    )
