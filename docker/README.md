### Docker assignment

There's a Flask app (```app.py```) in the  ```/second``` directory.
It provides 2 endpoints:
* / 
* /comments 

It has 2 pages:
```index.html```- the start page, where you can send the name and the comment.

```comments.html```- the page with comments.

HTML-files are in the ```./templates``` directory.

The data form the form isn't stored anywhere. 
The ```/comments``` page shows the default data:

```note
25     example = [Comment('asvezh', 'random text')]
```
The task:
1. Create a docker-comp
Задание:
1. Dockerize the app.
2. Improve the app that it can store the data from the input.
When restarting the container, the data must be saved!

####The additional task:
Improve data saving for the app.
Requirements:
1. Now the database should be deployed in a separate container.
2. The application should be able to start with ```docker-compose```.
3. The data entered into the form should be saved in the database and displayed on the ``/commemts`` page.



