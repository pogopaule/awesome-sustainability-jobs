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

jobs_with_corrdinats = jobs.filter(
    pl.col("lat").is_not_null() & pl.col("long").is_not_null()
)

st.dataframe(
    jobs,
    use_container_width=True,
    column_config={
        "website": st.column_config.LinkColumn(),
        "jobs": st.column_config.LinkColumn(),
        "review": st.column_config.LinkColumn(),
        "country": st.column_config.SelectboxColumn(),
    },
)
st.map(jobs_with_corrdinats, latitude="lat", longitude="long")
