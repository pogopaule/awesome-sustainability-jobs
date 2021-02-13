# Awesome Sustainability Jobs

A curated list of awesome dev jobs in the sustainability sector.\
[Contributions](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md) are highly appreciated. Especially for jobs outside of Germany.

{% for field in jobs.keys() -%}
- [{{field}}]({{toc_link(field)}})
{% endfor -%}
- [Jobportals](#jobportals)

---

sp. = speculative applications accepted\
re. = has at least one remote job offering

{% for field, jobsByCountry in jobs.items() -%}
## {{field}}

{% for country, jobs in jobsByCountry.items() -%}
### {{country}}

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

| portal | description |
| - | - |
{% for jobportal in jobportals -%}
| [{{jobportal.name}}]({{jobportal.website}}) | {{jobportal.description}} |
{% endfor %}

{% endfor %}
