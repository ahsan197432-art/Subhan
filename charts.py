import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def pie_chart(df):
    top = df["constructor_name"].value_counts().head(5)

    fig, ax = plt.subplots()
    ax.pie(
        top.values,
        labels=top.index,
        autopct="%1.1f%%"
    )
    ax.set_title("Top Constructors Distribution")

    st.pyplot(fig)


def histogram_chart(df):
    fig, ax = plt.subplots()

    sns.histplot(
        df["points"],
        bins=20,
        kde=True,
        ax=ax
    )

    ax.set_title("Points Distribution")

    st.pyplot(fig)


def line_chart(df):
    yearly = df.groupby("season")["points"].mean()

    fig, ax = plt.subplots()

    ax.plot(
        yearly.index,
        yearly.values,
        marker="o"
    )

    ax.set_title("Average Points by Season")
    ax.set_xlabel("Season")
    ax.set_ylabel("Average Points")

    st.pyplot(fig)


def bar_chart(df):
    top = (
        df.groupby("driver_name")["points"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=top.values,
        y=top.index,
        ax=ax
    )

    ax.set_title("Top Drivers by Points")
    ax.set_xlabel("Total Points")
    ax.set_ylabel("Driver")

    st.pyplot(fig)


def scatter_chart(df):
    fig, ax = plt.subplots()

    sns.scatterplot(
        data=df,
        x="grid_position",
        y="finish_position",
        ax=ax
    )

    ax.set_title("Grid Position vs Finish Position")
    ax.set_xlabel("Grid Position")
    ax.set_ylabel("Finish Position")

    st.pyplot(fig)


def box_plot(df):
    fig, ax = plt.subplots()

    sns.boxplot(
        x=df["points"],
        ax=ax
    )

    ax.set_title("Points Box Plot")

    st.pyplot(fig)


def heatmap_chart(df):
    numeric = df.select_dtypes(include="number")

    corr = numeric.corr()

    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        cmap="coolwarm",
        annot=False,
        ax=ax
    )

    ax.set_title("Correlation Heatmap")

    st.pyplot(fig)


def area_chart(df):
    yearly = df.groupby("season")["points"].sum()

    st.subheader("Total Points by Season")
    st.area_chart(yearly)


def count_plot(df):
    top = (
        df["driver_nationality"]
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    sns.barplot(
        x=top.values,
        y=top.index,
        ax=ax
    )

    ax.set_title("Top Driver Nationalities")
    ax.set_xlabel("Count")
    ax.set_ylabel("Nationality")

    st.pyplot(fig)


def violin_plot(df):
    fig, ax = plt.subplots()

    sns.violinplot(
        y=df["points"],
        ax=ax
    )

    ax.set_title("Points Distribution (Violin)")

    st.pyplot(fig)
