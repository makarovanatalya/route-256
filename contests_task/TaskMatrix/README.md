###Условия

Напишите функцию, которая "поворачивает" матрицу N*N, где 0 <= N < 6.

Пример:
rotate_matrix([[1, 2], [3, 4]])

Ответ:
[[3, 1], [4, 2]]


Для чтения и записи входных и выходных данных воспользуйтесь следующим шаблоном кода:

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