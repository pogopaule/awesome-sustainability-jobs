from enum import unique
import polars as pl
import streamlit as st
import yaml
from rich import pretty
import folium
from streamlit_folium import st_folium

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


selected_countries = st.sidebar.multiselect(
    "Filter countries", options=jobs["country"].unique().sort().to_list()
)

only_remote = st.sidebar.selectbox(
    "Filter remote column",
    [True, False],
    index=None,
    format_func=lambda o: "Only remote" if o else "Only non-remote",
)
only_speculative = st.sidebar.selectbox(
    "Filter speculative column",
    [True, False],
    index=None,
    format_func=lambda o: "Only speculative" if o else "Only non-speculative",
)

jobs = jobs.filter(
    (
        (pl.col("speculative") == only_speculative)
        if only_speculative is not None
        else True
    )
    & ((pl.col("remote") == only_remote) if only_remote is not None else True)
    & ((pl.col("country").is_in(selected_countries)) if selected_countries else True)
)

jobs_for_table = jobs.select(
    "name",
    "country",
    "website",
    "jobs",
    "remote",
    "speculative",
    "rating",
    "review",
).unique()


st.dataframe(
    jobs_for_table,
    use_container_width=True,
    column_config={
        "name": st.column_config.LinkColumn(label="Company Name"),
        "country": st.column_config.LinkColumn(label="Country"),
        "website": st.column_config.LinkColumn(label="Website", display_text="Link"),
        "remote": st.column_config.CheckboxColumn(label="Remote possible?"),
        "speculative": st.column_config.CheckboxColumn(
            label="Speculative applications?"
        ),
        "jobs": st.column_config.LinkColumn(label="Job Site", display_text="Link"),
        "review": st.column_config.LinkColumn(label="Review Site", display_text="Link"),
        "rating": st.column_config.NumberColumn(
            label="Rating",
        ),
    },
)

# TODO: focus row on map, don't reset zoom, focus pin in table, more info in popup?

jobs_for_map = jobs.filter(pl.col("lat").is_not_null() & pl.col("long").is_not_null())

m = folium.Map()
for row in jobs_for_map.iter_rows(named=True):
    folium.Marker(
        [row["lat"], row["long"]],
        popup=row["name"],
        tooltip=row["name"],
    ).add_to(m)

st_data = st_folium(m, use_container_width=True, returned_objects=[])
