#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, data) => {
  if (!error) {
    const results = JSON.parse(data).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});