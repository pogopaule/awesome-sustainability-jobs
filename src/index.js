const hbs = require('handlebars')
const fs = require('fs')
const yaml = require('js-yaml')
const _ = require('lodash')

function nest(seq, keys) {
    if (!keys.length) {
      return seq
    }
    let [ first, ...rest ] = keys
    return _.mapValues(_.groupBy(seq, first), value => nest(value, rest))
};

hbs.registerHelper('tocLink', (string) => string.toLowerCase().replace(/ /g, '-').replace(/[^a-zA-Z-]/g, ''))

const data = fs.readFileSync('data.yaml', 'utf8')
const templateScript = hbs.compile(fs.readFileSync('template.md', 'utf8'))

const dataJson = yaml.safeLoad(data)

const nestedJobs = nest(dataJson.jobs, ['field', 'country'])
const nestedJobportals = nest(dataJson.jobportals, ['country'])


const result = templateScript({jobs: nestedJobs, jobportals: nestedJobportals})

fs.writeFileSync('../README.md', result)
