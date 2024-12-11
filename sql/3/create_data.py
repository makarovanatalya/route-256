from random import choice

from faker import Faker
from sqlalchemy import (Column, Date, Enum, Integer, MetaData, String, Table,
                        create_engine, func, select)


def create_data():
    # created table

    engine = create_engine("postgresql://test:test@localhost:5432/test")

    meta = MetaData()

    animals = Table(
        'animals', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('type', Enum('dog', 'cat', name='type')),
        Column('name', String(length=70), nullable=False),
        Column('dob', Date, nullable=False),
        Column('sex', Enum('male', 'female', name='sex')),
        Column('owner_id', Integer, nullable=False)
    )
    meta.create_all(engine)

    # generated data for table

    fake = Faker()

    for _ in range(5):
        generated_type = choice(('dog', 'cat'))
        generated_sex = choice(('male', 'female'))

        if generated_sex == 'male':
            generated_name = fake.first_name_male()
        else:
            generated_name = fake.first_name_female()

        generated_dob = str(fake.date_between(start_date="-25y", end_date="now"))
        generated_owner_id = choice(range(1, 6))

        ins = animals.insert().values(type=generated_type, name=generated_name, dob=generated_dob, sex=generated_sex,
                                      owner_id=generated_owner_id)
        conn = engine.connect()
        conn.execute(ins)

    # count rows table

    s = select(func.count()).select_from(animals)
    conn = engine.connect()
    rows = conn.execute(s)

    for row in rows:
        count_animals = row[0]

    # choose random animal id

    random_animal_id = choice(range(1, count_animals))

    # select random animal

    s = select(animals.c).select_from(animals).where(animals.c.id == random_animal_id)
    conn = engine.connect()
    rows = conn.execute(s)
    conn.close()

    for row in rows:
        data_for_test = {
            'id': row['id'],
            'type': row['type'],
            'name': row['name'],
            'dob': row['dob'],
            'sex': row['sex'],
            'owner_id': row['owner_id'],
        }

    return data_for_test
