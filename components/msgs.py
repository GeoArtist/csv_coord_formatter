import streamlit as st


def center_line_position(color: str, background_color: str) -> str:
    return f"""display: flex;
        justify-content: center;
        margin: 0 auto;
        text-align: center;
        width: fit-content;
        
        background-color: {background_color};
        color: {color};
        padding: 10px;
        border-radius: 5px;"""


def window_center_position(color: str, background_color: str) -> str:
    return f"""position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        
        background-color: {background_color};
        color: {color};
        padding: 10px;
        border-radius: 5px;"""


def error_render(msg: str) -> None:
    BGCOLOR = "#ff4b4b"
    COLOR = "white"
    st.markdown(
        """
    <style>
    .error-box {
        """
        + center_line_position(COLOR, BGCOLOR)
        + """
    }
    </style>
    <div class="error-box">"""
        + msg
        + """</div>""",
        unsafe_allow_html=True,
    )


def info_render(msg: str) -> None:
    BGCOLOR = "#172d43"
    COLOR = "#90ddff"
    st.markdown(
        """
    <style>
    .info-box {
        """
        + center_line_position(COLOR, BGCOLOR)
        + """
    }
    </style>
    <div class="info-box">"""
        + msg
        + """</div>""",
        unsafe_allow_html=True,
    )


def warning_render(msg: str) -> None:
    BGCOLOR = "#3e3b16"
    COLOR = "#f9f9be"
    st.markdown(
        """
    <style>
    .warning-box {
        """
        + center_line_position(COLOR, BGCOLOR)
        + """
    }
    </style>
    <div class="warning-box">"""
        + msg
        + """</div>""",
        unsafe_allow_html=True,
    )


def success_render(msg: str) -> None:
    BGCOLOR = "#173928"
    COLOR = "#dffdc9"
    st.markdown(
        """
    <style>
    .success-box {
        """
        + center_line_position(COLOR, BGCOLOR)
        + """
    }
    </style>
    <div class="success-box">"""
        + msg
        + """</div>""",
        unsafe_allow_html=True,
    )
