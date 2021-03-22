# Awesome Sustainability Jobs

A curated list of awesome dev jobs in the sustainability sector.\
[Contributions](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md) are highly appreciated. Especially for jobs outside of Germany.

Looking for open source projects instead? [Go here](https://github.com/protontypes/open-sustainable-technology)

{% for country in jobs.keys() -%}
- [{{country}}]({{toc_link(country)}})
{% endfor -%}
- [Jobportals](#jobportals)

---

sp. = speculative applications accepted\
re. = has at least one remote job offering

{% for country, jobsByCountry in jobs.items() -%}
## {{country}}

{% for field, jobs in jobsByCountry.items() -%}
### {{field}}

| company | jobs | rating | description | sp. | re. |
| - | - | - | - | - | - |
{% for job in jobs -%}
| [{{job.name}}]({{job.website}}) | [jobs]({{job.jobs}}) | {% if job.review %}[{{job.rating}}/5]({{job.review}}){% endif %} | {{job.description}} | {% if job.speculative %}✅{% endif %} | {% if job.remote %}✅{% endif %} |
{% endfor %}

{% endfor %}

{% endfor %}

## Jobportals

{% for country, jobportals in jobportals.items() -%}
### {{country}}

{% for jobportal in jobportals -%}
* [{{jobportal.name}}]({{jobportal.website}})
{% endfor %}

{% endfor %}
