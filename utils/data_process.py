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

    df.index.name = "Nr"
    cur_columns = df.columns
    new_columns: list[str] = ["X", "Y", "H"]
    # Ensure new_columns has the same length as cur_columns
    if len(new_columns) < len(cur_columns):
        new_columns.extend([""] * (len(cur_columns) - len(new_columns)))
        df.columns = new_columns
        df = df[["X", "Y", "H"]]

    # Round Coordinates
    df["X"] = df["X"].apply(lambda x: f"{x:.{st.session_state["x_y_round"]}f}")
    df["Y"] = df["Y"].apply(lambda x: f"{x:.{st.session_state["x_y_round"]}f}")
    df["H"] = df["H"].apply(lambda x: f"{x:.{st.session_state["h_round"]}f}")

    return df
