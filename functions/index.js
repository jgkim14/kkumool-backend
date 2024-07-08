const functions = require('firebase-functions');
const main = require('./main');

exports.myFunction = functions.https.onRequest(main.myFunction);
