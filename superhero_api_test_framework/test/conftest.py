import random

import pytest

from superhero_api_test_framework.clients.api_client import ApiClient


@pytest.fixture
def find_hero_with_power():
    hero_id_compare = []

    while len(hero_id_compare) != 2:
        random_id = random.randint(1, 700)
        if ApiClient().get_by_powerstats(random_id).json().get('power') != 'null':
            hero_id_compare.append(ApiClient().get_by_powerstats(random_id).json().get('id'))

    power_1 = int(ApiClient().get_by_powerstats(hero_id_compare[0]).json().get('power'))
    power_2 = int(ApiClient().get_by_powerstats(hero_id_compare[1]).json().get('power'))

    if power_1 > power_2:
        winner_name = ApiClient().get_by_powerstats(hero_id_compare[0]).json().get('name')
    else:
        winner_name = ApiClient().get_by_powerstats(hero_id_compare[1]).json().get('name')

    return hero_id_compare, winner_name
