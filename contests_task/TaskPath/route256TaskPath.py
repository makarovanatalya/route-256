import json


def get_by_dotted_path(container, path: str):

    for point in path.split('.'):

        if point == '':
            return None

        if type(container) == list:
            try:
                container = container[int(point)]
            except LookupError:
                raise LookupError
            except ValueError:
                raise LookupError

        elif type(container) == dict:
            if container.get(point) is None:
                raise LookupError
            container = container.get(point)

    return container


if __name__ == "__main__":
    input_str = input()
    [container, path] = json.loads(input_str)

    try:
        answer = get_by_dotted_path(container, path)
    except LookupError:
        answer = 'LookupError'

    print(json.dumps(answer))
