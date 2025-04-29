from enum import unique
import polars as pl
import streamlit as st
import yaml
from rich import pretty

pretty.install()


def read_jobs_yaml() -> pl.DataFrame:
    with open("jobs.yaml", "r") as file:
        data = yaml.safe_load(file)
        return (
            pl.from_dicts(data)
            .with_columns(
                [
                    pl.col("rating").cast(pl.Float64),
                    pl.col("remote").cast(pl.Boolean),
                    pl.col("speculative").cast(pl.Boolean),
                ]
            )
            .explode("geo")
            .unnest("geo")
        )


def read_portals_yaml() -> pl.DataFrame:
    with open("portals.yaml", "r") as file:
        data = yaml.safe_load(file)
        return pl.from_dicts(data)


jobs = read_jobs_yaml()
portals = read_portals_yaml()


only_remote = st.checkbox("Only remote jobs", value=False)
only_speculative = st.checkbox("Only speculative jobs", value=False)
selected_countries = st.multiselect(
    "Select countries", options=jobs["country"].unique().sort().to_list()
)

jobs_for_table = (
    jobs.select(
        "name",
        "country",
        "website",
        "jobs",
        "remote",
        "speculative",
        "rating",
        "review",
    )
    .filter(
        ((pl.col("speculative") == only_speculative) if only_speculative else True)
        & ((pl.col("remote") == only_remote) if only_remote else True)
        & (
            (pl.col("country").is_in(selected_countries))
            if selected_countries
            else True
        )
    )
    .unique()
)

jobs_for_map = jobs.filter(pl.col("lat").is_not_null() & pl.col("long").is_not_null())


st.dataframe(
    jobs_for_table,
    use_container_width=True,
    column_config={
        "website": st.column_config.LinkColumn(label="Website", display_text="Link"),
        "jobs": st.column_config.LinkColumn(label="Job Site", display_text="Link"),
        "review": st.column_config.LinkColumn(label="Review Site", display_text="Link"),
    },
)
st.map(
    jobs_for_map,
    latitude="lat",
    longitude="long",
)
