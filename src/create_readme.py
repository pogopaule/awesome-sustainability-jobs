import yaml
import itertools
from jinja2 import Template
import re

def nest(seq, keys):
    if not keys:
        return seq

    first, *rest = keys

    keyfunc = lambda x: x[first]
    grouped = itertools.groupby(sorted(seq, key=keyfunc), key=keyfunc)
    result = {}
    for k, v in grouped:
        result[k] = nest(list(v), rest)

    return result

def tocLink(link):
    return "#" + re.sub(r"[^a-zA-Z-]", '', link.lower().replace(' ', '-'))



with open("data.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)

        nestedJobs = nest(data['jobs'], ['field', 'country'])
        fields = nestedJobs.keys()
        nestedJobportals = nest(data['jobportals'], ['country'])

        template = Template(open('template.md').read())

        readme = template.render(jobs=nestedJobs, jobportals=nestedJobportals, tocLink=tocLink)

        with open("../README.md", "w") as readme_file:
            readme_file.write(readme)

    except yaml.YAMLError as error:
        print(error)




