#!/usr/bin/env node
var zippy = require('./')
var path = require('path')
var argv = require('minimist')(process.argv.slice(2), {
  alias: { help: 'h' }
})

if (argv.help) {
  require('fs')
    .createReadStream(path.join(__dirname, 'help.txt'))
    .pipe(process.stdout)
} else {
  console.log(argv.all ? zippy.quotes.join('\n') : zippy())
}
