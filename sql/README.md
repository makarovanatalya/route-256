## SQL assignment

### 1. The oldest user.
In the table:
```sql
CREATE TABLE users
(
    id   serial,
    name varchar(40),
    age  integer
);
```
Find the name of the oldest user.

### 2. Where are users?
In 2 related tables:
```sql
CREATE TABLE users
(
    id          serial primary key,
    name        varchar(40),
    location_id integer # foreign key
);
CREATE TABLE location
(
    id          serial primary key,
    name        varchar(40)
);
```
Find 10 names of the users that live in Moscow.

### 3. Data preparation.
Develop a test that connects to a local DB, creates the animals table (the table should have at least 5 columns of different types).
Fill the table with 5 different animals.
Get one of the rows (in the test) and check that they are correct.
