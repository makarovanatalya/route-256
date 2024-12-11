import datetime

from create_data import create_data
from hamcrest import (assert_that, greater_than_or_equal_to, has_key,
                      instance_of, is_in, less_than_or_equal_to)


def test_create_data():
    test_data = create_data()

    # check structure

    assert_that(test_data, has_key('id'))
    assert_that(test_data, has_key('type'))
    assert_that(test_data, has_key('name'))
    assert_that(test_data, has_key('dob'))
    assert_that(test_data, has_key('sex'))
    assert_that(test_data, has_key('owner_id'))

    # check types

    assert_that(test_data['id'], instance_of(int), reason='Animal ID is not int')
    assert_that(test_data['owner_id'], instance_of(int), reason='Owner ID is not int')

    assert_that(test_data['name'], instance_of(str), reason='Name is not str')
    assert_that(test_data['type'], instance_of(str), reason='Type is not str')
    assert_that(test_data['sex'], instance_of(str), reason='Sex is not str')

    assert_that(test_data['dob'], instance_of(datetime.date), reason='Date of birth is not date')

    # check requirements

    assert_that(test_data['type'], is_in(('cat', 'dog')), reason='Wrong type')
    assert_that(test_data['sex'], is_in(('male', 'female')), reason='Wrong sex')

    assert_that(test_data['dob'] > datetime.date(1990, 1, 1), reason='Animals do not live that long :(')

    assert_that(len(test_data['name']), less_than_or_equal_to(70), reason='Name is longer than 70 characters')
    assert_that(len(test_data['name']), greater_than_or_equal_to(1), reason='Empty name')



