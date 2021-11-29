from hamcrest import assert_that, equal_to

from superhero_api_test_framework.clients.api_client import ApiClient


def test_superhero_example(find_hero_with_power):
    test_id_1 = find_hero_with_power[0][0]
    test_id_2 = find_hero_with_power[0][1]
    test_winner_name = find_hero_with_power[1]

    power_1 = int(ApiClient().get_by_id(test_id_1).json().get('powerstats').get('power'))
    power_2 = int(ApiClient().get_by_id(test_id_2).json().get('powerstats').get('power'))

    if power_1 > power_2:
        winner_name = ApiClient().get_by_id(test_id_1).json().get('name')
    else:
        winner_name = ApiClient().get_by_id(test_id_2).json().get('name')

    assert_that(winner_name, equal_to(test_winner_name),
                reason=f'{test_winner_name} should have won, but {winner_name} won')
