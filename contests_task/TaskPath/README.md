###Conditions

Write a function that gets a nested object in a dictionary or list by a string path.

For example:

get_by_dotted_path({'a': {'b': [1, 2]}}, 'a.b.1')

Answer:
2

If you try to access it incorrectly, for example
get_by_dotted_path({'a': {'b': []}}, 'a.c')
you should throw `LookupError`.
If the string is empty, return `None`.

###Limitations:
Only dictionaries and lists / their combinations are accepted as input.
All dictionary keys are always strings, keys should not contain '.'
The solution should not have more than three levels of nesting.

Use the following code template to read and write input and output data:
```

import json


def get_by_dotted_path(container, path: str):
    # TODO insert you code


if __name__ == "__main__":
    input_str = input()
    [container, path] = json.loads(input_str)

    try:
        answer = get_by_dotted_path(container, path)
    except LookupError:
        answer = 'LookupError'

    print(json.dumps(answer))

```