# Awesome Sustainability Jobs

A curated list of awesome dev jobs in the sustainability sector.\
[Contributions](https://github.com/pogopaule/awesome-sustainability-jobs/blob/main/CONTRIBUTING.md) are highly appreciated. Especially for jobs outside of Germany.

{{#each jobs}}
- [{{@key}}](#{{tocLink @key}})
{{/each}}
- [Jobportals](#jobportals)

---

*spec.* = speculative applications accepted\
*remote* = has at least one remote job offering

{{#each jobs}}
## {{@key}}

| company | jobs | description | spec. | remote | country |
| - | - | - | - | - | - |
{{#each this}}
| [{{{name}}}]({{{website}}}) | [jobs]({{{jobs}}}) | {{{description}}} | {{#if speculative}}✅{{/if}} | {{#if remote}}✅{{/if}} | {{{country}}}
{{/each}}

{{/each}}

## Jobportals

| portal | description | country |
| - | - | - |
{{#each jobportals}}
| [{{{name}}}]({{{website}}}) | {{{description}}} | {{{country}}} |
{{/each}}
