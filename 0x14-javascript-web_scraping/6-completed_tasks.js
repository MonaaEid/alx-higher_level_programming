#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTodos = todos.filter(todo => todo.completed);
    const completedTodosByUser = completedTodos.reduce((acc, todo) => {
      if (acc[todo.userId]) {
        acc[todo.userId]++;
      } else {
        acc[todo.userId] = 1;
      }
      return acc;
    }, {});
    Object.entries(completedTodosByUser).forEach(([userId, numCompleted]) => {
      console.log(`User ${userId} has completed ${numCompleted} tasks.`);
    });
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
