## Задание по SQL

### 1. Самый взрослый пользователь.
Дана таблица:
```sql
CREATE TABLE users
(
    id   serial,
    name varchar(40),
    age  integer
);
```
Напишите запрос, который покажет имя самого взрослого пользователя в таблице

### 2. Где пользователи?
Даны связанные таблицы таблицы:
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
Напишите запрос, который покажет 10 имен пользователей, которые живут в Москве

### 3. Подготовка данных.
Нужно написать тест на Python, который подключается к локальной базе данных, создает таблицу animals (Добавьте минимум 5 полей разного типа. Поля и типы придумайте на свое усмотрение).
После этого заполните таблицу 5 разными животными.
После получите из таблицы одну из записей. И проверьте в тесте, что полученные поля корректны с помощью использования assert. Тест должен проходить. Чем разнообразнее проверки будут - тем лучше.