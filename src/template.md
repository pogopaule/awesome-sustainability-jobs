# Awesome Sustainability Jobs

A curated list of companies in the sustainability sector with jobs for devs.

> The best minds of our generation are thinking about ~~how to make people click on ads~~ climate change\
> [Electricity Maps](https://www.electricitymaps.com/jobs)

**This project needs your help** and [contributions](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md):
- Share this project with others
- Add a link to [the backlog](https://pad.disroot.org/p/awesome-sustainability-jobs)
- Fix broken links
- Review links in the [backlog](https://pad.disroot.org/p/awesome-sustainability-jobs) and [add them](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/src/data.yaml) to this project
- Suggest structural improvements by opening a pull request with changes to [template.md](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/src/template.md)

Not able to work on sustainability in a full time job? Check out this list of [open source projects](https://github.com/protontypes/open-sustainable-technology).

---

## All companies on a map

![preview image of map](map.jpg)

[Show companies on a map](https://awesome-sustainability-jobs.netlify.app/) 🗺️

## All companies in a list

{% for country in jobs.keys() -%}
- [{{country}}]({{toc_link(country)}})
{% endfor -%}
- [Jobportals](#jobportals)

{% for country, jobsByCountry in jobs.items() -%}
### {{country}}

{% for field, jobs in jobsByCountry.items() -%}
#### {{field}}

| company | jobs | rating[*](#Legend) | description | sp[*](#Legend)| re[*](#Legend) |
| - | - | - | - | - | - |
{% for job in jobs -%}
| [{{job.name}}]({{job.website}}) | [jobs]({{job.jobs}}) | {% if job.review %}[{{job.rating}}/5]({{job.review}}){% endif %} | {{job.description}} | {% if job.speculative %}✅{% endif %} | {% if job.remote %}✅{% endif %} |
{% endfor %}

{% endfor %}

{% endfor %}

#### Legend

* rating: Rating by the employees according to portals like [Kununu](https://www.kununu.com/) or [glassdoor](https://www.glassdoor.com/)
* sp: speculative applications accepted
* re: has at least one remote job offering

## Jobportals

{% for country, jobportals in jobportals.items() -%}
### {{country}}

{% for jobportal in jobportals -%}
* [{{jobportal.name}}]({{jobportal.website}})
{% endfor %}

{% endfor %}
