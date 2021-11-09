import re
from itertools import groupby

import yaml
from jinja2 import Template

from utils import map_reduce, denormalize


def nest(seq, keys):
    if not keys:
        return seq

    first_key, *rest_keys = keys

    keyfunc = lambda x: x[first_key]
    grouped = groupby(sorted(seq, key=keyfunc), key=keyfunc)
    result = {}
    for key, value in grouped:
        result[key] = nest(list(value), rest_keys)

    return result


def toc_link(link):
    return "#" + re.sub(r"[^a-zA-Z-]", "", link.lower().replace(" ", "-"))


def composed(f, g):
    return lambda x: f(g(x))


def unique_by_country(l):
    return {k['country']: k for k in l}.values()


def remove_duplicate_country_entry(job):
    job['geo'] = unique_by_country(job['geo'])
    return job


with open("data.yaml", "r") as stream:
    try:
        DATA = yaml.safe_load(stream)

        DENORMALIZED_JOBS = map_reduce(composed(denormalize, remove_duplicate_country_entry), DATA["jobs"])

        NESTED_JOBS = nest(DENORMALIZED_JOBS, ["country", "field"])
        FIELDS = NESTED_JOBS.keys()
        NESTED_JOBPORTALS = nest(DATA["jobportals"], ["country"])

        TEMPLATE = Template(open("template.md").read())

        README = TEMPLATE.render(
            jobs=NESTED_JOBS, jobportals=NESTED_JOBPORTALS, toc_link=toc_link
        )

        with open("../README.md", "w") as readme_file:
            readme_file.write(README)

    except yaml.YAMLError as error:
        print(error)
