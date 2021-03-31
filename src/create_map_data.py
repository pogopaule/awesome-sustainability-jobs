import yaml
from jinja2 import Template


with open("data.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)

        companies = data["jobs"]

        with open("../map-data.js", "w") as map_data:
            map_data.write("locations = [\n")

            for company in companies:
                geo = company["geo"]
                for location in geo:
                    if location["lat"]:
                        name = company["name"]
                        lat = location["lat"]
                        long = location["long"]
                        map_data.write(f"  ['{name}',{lat},{long}],\n")

            map_data.write("]\n")

    except yaml.YAMLError as error:
        print(error)
