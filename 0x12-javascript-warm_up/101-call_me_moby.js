#!/usr/bin/node
/*
   A JavaScript module that exports a function named callMeMoby
   which executes a given function x times.
*/

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
