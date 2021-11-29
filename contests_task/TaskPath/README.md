###Условия

Напишите функцию, которая по строковому пути получает вложенный объект в словаре или списке.

Например: 
get_by_dotted_path({'a': {'b': [1, 2]}}, 'a.b.1')

Ответ:
2

При попытке некорректного обращения, например
get_by_dotted_path({'a': {'b': []}}, 'a.c')
нужно выбрасывать `LookupError`.
При пустой строке — возвращать `None`.


####Ограничения:
На вход подаются только словари и списки / их комбинации.
Все ключи словарей — всегда строки, ключи не должны содержать '.'
Решение не должно иметь больше трех уровней вложенности.

Для чтения и записи входных и выходных данных воспользуйтесь следующим шаблоном кода:

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