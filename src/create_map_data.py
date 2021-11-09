import yaml
import json
from jinja2 import Template
from utils import map_reduce, denormalize

with open("data.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)

        companies = map_reduce(denormalize, data["jobs"])

        with open("../map/map-data.js", "w") as map_data:
            map_data.write("locations = [\n")

            for company in companies:
                if company["geo"]["lat"]:
                    company_json = json.dumps(company)
                    map_data.write(f"  {company_json},\n")

            map_data.write("]\n")

    except yaml.YAMLError as error:
        print(error)
