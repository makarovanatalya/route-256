###Conditions

A task for Python developers. Write a function that will convert a number to the format used in Excel.
Examples:
`1 -> A`, `2 -> B`, `26 -> Z`, `27 -> AA`, `28 -> AB`

Input data boundary:
from 1 to 255 inclusive

To read and write input and output data, use the following code template:

```

import json


def to_excel_format(number: int) -> str:
    # TODO insert you code
    pass


if __name__ == "__main__":
    input_str = input()
    number = int(input_str)

    answer = to_excel_format(number)

    print(json.dumps(answer))

```
###Input data format

The function input is an integer number in the range from 1 to 255 inclusive.

###Output data format

The output must be a sequence of characters.