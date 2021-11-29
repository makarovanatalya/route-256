
import json


def rotate_matrix(matrix):
    new_matrix = []

    for i in range(len(matrix)):
        new_matrix.append([])
        for matrix_line in reversed(matrix):
            new_matrix[i].append(matrix_line[i])

    return new_matrix


if __name__ == "__main__":
    input_str = input()
    matrix = json.loads(input_str)

    answer = rotate_matrix(matrix)

    print(json.dumps(answer))
