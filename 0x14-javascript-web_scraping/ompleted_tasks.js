#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
// - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// - Only print users with completed task
// - You must use the module request

const request = require('request');
const APIurl = process.argv[2];

request(APIurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const todolist = JSON.parse(body);
    for (const i in todolist) {
      const todo = todolist[i];
      if (todo.completed === true) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
