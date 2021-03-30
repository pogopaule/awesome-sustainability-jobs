import re
from itertools import groupby
import yaml
from jinja2 import Template
from functools import reduce

flat_map = lambda f, xs: reduce(lambda a, b: a + b, map(f, xs))


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


def denormalize(job):
    result = []
    for location in job["geo"]:
        job_copy = job.copy()
        del job_copy["geo"]
        job_copy["country"] = location["country"]
        job_copy["geo"] = {"lat": location["lat"], "long": location["long"]}
        result.append(job_copy)

    return result


with open("data.yaml", "r") as stream:
    try:
        DATA = yaml.safe_load(stream)

        DENORMALIZED_JOBS = flat_map(denormalize, DATA["jobs"])
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
