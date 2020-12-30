const hbs = require('handlebars')
const fs = require('fs')
const yaml = require('js-yaml')
const _ = require('underscore')


hbs.registerHelper('tocLink', (string) => string.toLowerCase().replace(' ', '-').replace('.', ''))

const data = fs.readFileSync('data.yaml', 'utf8')
const templateScript = hbs.compile(fs.readFileSync('template.md', 'utf8'))

const dataJson = yaml.safeLoad(data)

const jobsByField = _.groupBy(dataJson.jobs, 'field')


const result = templateScript({jobs: jobsByField, jobportals: dataJson.jobportals})

fs.writeFileSync('../README.md', result)
