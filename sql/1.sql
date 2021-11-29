SELECT name
FROM   users
WHERE  age = (SELECT MAX(age)
              FROM   users)
LIMIT 1;