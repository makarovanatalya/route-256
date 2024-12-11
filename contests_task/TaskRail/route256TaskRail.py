inputData = list(map(int, input().split()))

# inputData[0] - the max length of skirting board, n
# inputData[1] - the needed length, L

if inputData[1] < inputData[0]:
    nRail = inputData[1]
else:
    nRail = inputData[1] // inputData[0]

    if inputData[1] % inputData[0] != 0:
        nRail += 1

print(nRail)
