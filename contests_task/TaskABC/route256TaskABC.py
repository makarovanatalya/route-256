import json


def to_excel_format(number: int) -> str:
    if number <= 0 or number > 256:
        return ''
    else:
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if number <= 26:
            cell = abc[number-1]
        elif number % 26 == 0:
            cell = abc[(number // 26)-2] + abc[25]
        else:
            cell = abc[(number // 26)-1] + abc[(number % 26)-1]
        return cell

    pass


if __name__ == "__main__":
    input_str = input()
    number = int(input_str)

    answer = to_excel_format(number)

    print(json.dumps(answer))
