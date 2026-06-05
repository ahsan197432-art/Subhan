import streamlit as st
import pandas as pd

def apply_filters(df):

    st.sidebar.header("Dashboard Filters")

    df["race_date"] = pd.to_datetime(
        df["race_date"],
        errors="coerce"
    )

    # Season Filter
    seasons = sorted(df["season"].unique())

    selected_seasons = st.sidebar.multiselect(
        "Season",
        seasons,
        default=seasons
    )

    # Constructor Filter
    constructors = sorted(df["constructor_name"].dropna().unique())

    selected_constructors = st.sidebar.multiselect(
        "Constructor",
        constructors,
        default=constructors[:10]
    )

    # Driver Search
    driver_search = st.sidebar.text_input(
        "Search Driver"
    )

    # Points Range
    min_points = int(df["points"].min())
    max_points = int(df["points"].max())

    points_range = st.sidebar.slider(
        "Points Range",
        min_points,
        max_points,
        (min_points, max_points)
    )

    filtered = df.copy()

    filtered = filtered[
        filtered["season"].isin(selected_seasons)
    ]

    filtered = filtered[
        filtered["constructor_name"].isin(selected_constructors)
    ]

    filtered = filtered[
        filtered["points"].between(
            points_range[0],
            points_range[1]
        )
    ]

    if driver_search:
        filtered = filtered[
            filtered["driver_name"]
            .str.contains(driver_search,
                          case=False,
                          na=False)
        ]

    if st.sidebar.button("Reset Filters"):
        st.rerun()

    return filtered