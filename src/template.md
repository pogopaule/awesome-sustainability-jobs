# Awesome Sustainability Jobs

A curated list of dev jobs in the sustainability sector.

[Contributions](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md) are highly appreciated. Especially for jobs outside of Germany.

Ways to contribute:
- Add a link to [the backlog list](https://pad.disroot.org/p/awesome-sustainability-jobs)
- Review links in the [backlog](https://pad.disroot.org/p/awesome-sustainability-jobs) and [contribute](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md) them to [data.yml](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/src/data.yaml)
- Suggest structural improvements by opening a pull request with changes to [template.md](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/src/template.md)
- Fix broken links
- Show this project to others

Looking for open source projects instead? [Go here](https://github.com/protontypes/open-sustainable-technology)

---

## Map

![preview image of map](map.jpg)

[Show companies on a map](https://awesome-sustainability-jobs.netlify.app/) 🗺️

## List

{% for country in jobs.keys() -%}
- [{{country}}]({{toc_link(country)}})
{% endfor -%}
- [Jobportals](#jobportals)


sp. = speculative applications accepted\
re. = has at least one remote job offering

{% for country, jobsByCountry in jobs.items() -%}
### {{country}}

{% for field, jobs in jobsByCountry.items() -%}
#### {{field}}

| company | jobs | rating | description | sp. | re. |
| - | - | - | - | - | - |
{% for job in jobs -%}
| [{{job.name}}]({{job.website}}) | [jobs]({{job.jobs}}) | {% if job.review %}[{{job.rating}}/5]({{job.review}}){% endif %} | {{job.description}} | {% if job.speculative %}✅{% endif %} | {% if job.remote %}✅{% endif %} |
{% endfor %}

{% endfor %}

{% endfor %}

### Jobportals

{% for country, jobportals in jobportals.items() -%}
#### {{country}}

{% for jobportal in jobportals -%}
* [{{jobportal.name}}]({{jobportal.website}})
{% endfor %}

{% endfor %}
