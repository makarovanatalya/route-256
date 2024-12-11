###1. Develop a test.

Develop a parameterized test sends a request to:

```https://superheroapi.com/api/<access-token>/id```


Requirements:
* Implement a http-client for **superheroapi.com**.
* Use a list of 5 random numbers in the range [1-700] for parametrizing.


###2. Implement a quick check decorator.

Implement a **@smoke_check** decorator to be called before a test.

It should check that:
* the response code is okay;
* the **response** field contains the **success** status;
* the decorator should be placed in the **checkers** directory.

The example:

```
import pytest

@pytest.mark.parametrize(...)
@smoke_check
def test_superhero_example(*args):
    ...
    return response
```

###3. Develop a test "woman is woman?".

Implement a function that gets the data from:

**https://www.superheroapi.com/ids.html**

and gets from here names that contain "**Woman**" (non-case-sensitive search)

For example:
```json
Bionic Woman
Hawkwoman
Batwoman V
```

This data should be used for parametrizing the test.

The test should:
1. Get info about a superhero: ```https://superheroapi.com/api/<access-token>/id```

2. Check that their gender (**appearance/gender**) is **Female**.

Requirements:
* Use the **pyHamcrest** library for assertions.
* Use a http-client for **superheroapi.com**.
* Use the **re** library for parsing superheroes page.

###4. Develop a test "Batman vs Superman" with a fixture.

Develop a test that compares power of superheroes.

Not all superheroes have all characteristics, needs to develop a fixture to prepare the data.
The fixture should:
* get a random number in the range [1-700]
* check that this superhero has not null **power**:

```https://www.superheroapi.com/api.php/<access-token>/id/powerstats```

* in case of success, repeat the same for the second superhero.

Then the **who_stronged** function should be called (form the fixture) which should
1. Compare superheroes by the ```power``` parameter.
2. Return (```name```) of the strongest superhero.

The fixture should return: 2 ids, and the name of the winner.

The example of the data from API:

```json
{
    "response": "success",
    "id": "505",
    "name": "Oracle",
    "intelligence": "75",
    "strength": "11",
    "speed": "23",
    "durability": "28",
    "power": "19",
    "combat": "76"
}
```

The test should:

1. Send a request for each ID: ```https://www.superheroapi.com/api.php/<access-token>/id```
2. Compare ```powerstats/power``` for them.
3. Get the winner's name.
4. Compare the result with the result for the fixture (it should be equal).
