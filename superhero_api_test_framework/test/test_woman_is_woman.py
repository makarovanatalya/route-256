import pytest
from hamcrest import assert_that, equal_to

from superhero_api_test_framework.clients.api_client import ApiClient
from superhero_api_test_framework.helpers.parsing_woman import parse_women


@pytest.mark.parametrize('iterate', parse_women())
def test_superhero_example(iterate):
    response = ApiClient().get_by_id(iterate)
    hero_gender = response.json().get('appearance').get('gender')
    assert_that(hero_gender, equal_to('Female'), reason='Hero is not a woman')

    return response
