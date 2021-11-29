SELECT u.name
FROM users AS u
JOIN location as l
ON u.location_id = l.id
WHERE l.name = 'Moscow'
LIMIT 10;