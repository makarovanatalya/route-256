def defineNumber(inputNumber):
    if inputNumber < 11:
        return False

    lenNumber = len(str(inputNumber))

    for i in range(lenNumber, 1, -1):
        if inputNumber % int('1' * i) == 0:
            return True

    for i in range(lenNumber, 1, -1):
        if inputNumber - int('1' * i) >= 0:
            if defineNumber(inputNumber - int('1' * i)):
                return True


for i in range(int(input())):
    inputNumber = int(input())

    if defineNumber(inputNumber):
        print('YES')
    else:
        print('NO')
