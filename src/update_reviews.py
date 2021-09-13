import requests
import time
import random

import oyaml as yaml

# https://github.com/yaml/pyyaml/issues/234#issuecomment-765894586
class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


# https://stackoverflow.com/questions/37200150/can-i-dump-blank-instead-of-null-in-yaml-pyyaml
def represent_none(self, _):
    return self.represent_scalar("tag:yaml.org,2002:null", "")


def dump_data(data):
    with open("data.yaml", "w") as file:
        yaml.dump(data, file, allow_unicode=True, width=10000, Dumper=Dumper)


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}
yaml.add_representer(type(None), represent_none)

with open("data.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)

        jobs = data["jobs"]

        for index, job in enumerate(jobs):
            url = job["review"]
            job["rating"] = None

            if url and url.startswith("https://www.kununu"):
                print(url + ": ", end="", flush=True)
                response = requests.get(url, headers=headers)
                content = response.text
                index = content.find('<span class="index__value__')
                try:
                    offset = 56
                    rating = float(
                            content[index + offset : index + offset + 3].replace(",", ".")
                            )
                except ValueError as error:
                    print(error)
                print(rating)
                job["rating"] = rating
                time.sleep(random.randint(1, 4))

        dump_data(data)

    except yaml.YAMLError as error:
        print(error)
