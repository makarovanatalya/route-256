inputData = list(map(int, input().split()))

# inputData[0] - максимальная длина рейки n
# inputData[1] - необходимая длина L

if inputData[1] < inputData[0]:
    nRail = inputData[1]
else:
    nRail = inputData[1] // inputData[0]

    if inputData[1] % inputData[0] != 0:
        nRail += 1

print(nRail)
