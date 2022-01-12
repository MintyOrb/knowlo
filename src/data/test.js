let data = require('./resources.json')
console.log(data.length)
for(x in data[0]["collect(distinct t)"]){
    console.log(data[0]["collect(distinct t)"][x]['properties']['english'])
}