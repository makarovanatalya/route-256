nBoxes = int(input())
weightBoxes = list(map(int, input().split()))
weightBoxes.sort()

minWeight = 0

for i in range(1, nBoxes, 2):
    minWeight += weightBoxes[i]-weightBoxes[i-1]

print(minWeight)
