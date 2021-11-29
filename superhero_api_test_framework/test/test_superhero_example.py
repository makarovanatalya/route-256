import random

import pytest

from superhero_api_test_framework.checkers.checkers import smoke_check
from superhero_api_test_framework.clients.api_client import ApiClient

random_id = random.sample(range(1, 700), 5)


@pytest.mark.parametrize('iterate', random_id)
@smoke_check
def test_superhero_example(iterate):
    response = ApiClient().get_by_id(iterate)
    return response
