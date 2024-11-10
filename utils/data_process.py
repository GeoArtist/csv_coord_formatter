import pandas as pd
import streamlit as st


def process(df: pd.DataFrame) -> pd.DataFrame:
    """Main workflow data process

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame

    """

    df = df.iloc[:, :3]
    df = df.copy(deep=True)
    df.rename(columns={1: "X", 2: "Y", 3: "H"}, inplace=True)
    df.index.name = "Nr"

    # Round Coordinates
    df["X"] = df["X"].apply(lambda x: f"{x:.{st.session_state["x_y_round"]}f}")
    df["Y"] = df["Y"].apply(lambda y: f"{y:.{st.session_state["x_y_round"]}f}")
    df["H"] = df["H"].apply(lambda h: f"{h:.{st.session_state["h_round"]}f}")

    return df
