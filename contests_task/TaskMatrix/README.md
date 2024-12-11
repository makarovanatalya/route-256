###Conditions

Write a function that "rotates" an N*N matrix, where 0 <= N < 6.

Example:
rotate_matrix([[1, 2], [3, 4]])

Answer:
[[3, 1], [4, 2]]

Use the following code template to read and write input and output data:

```

import json


def rotate_matrix(matrix):
    # TODO insert you code
    return []


if __name__ == "__main__":
    input_str = input()
    matrix = json.loads(input_str)

    answer = rotate_matrix(matrix)
    
    print(json.dumps(answer))

```