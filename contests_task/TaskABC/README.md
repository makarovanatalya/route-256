###Условия

Задача для Python-разработчиков. Напишите функцию, которая переведет число в формат представления, использующийся в Excel.
Примеры:
`1 -> A`, `2 -> B`, `26 -> Z`, `27 -> AA`, `28 -> AB`

Граница входных данных:
от 1 до 255 включительно

Для чтения и записи входных и выходных данных воспользуйтесь следующим шаблоном кода:

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


###Формат входных данных

На вход функции подается целое число, входящее в диапазон от 1 до 255 включительно.


###Формат выходных данных

На выходе должна быть последовательность символов.

