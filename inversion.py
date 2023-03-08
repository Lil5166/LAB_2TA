inputFile = open("input.txt") # вхідний файл
outputFile = open("output.txt", "w") # вихідний файл
index = int(input()) #запит на користувача
inputArray = []
outputArray = [[index]]
def inversion(something): # використовуємо метод інверсії
    inversion = 0
    temporaryArr = []
    for i in range(inputArray[0][1]):
        temporaryArr.append(inputArray[something][inputArray[index].index(i + 1, 1)])
    for i in range(len(temporaryArr)):
        for j in range(i, len(temporaryArr)):
            if temporaryArr[i] > temporaryArr[j]:
                inversion += 1
    return inversion


def arraySort(arr): # сортуємо масив
    for i in range(1, inputArray[0][0]):
        for j in range(1, inputArray[0][0] - i):
            if outputArray[j][1] > outputArray[j + 1][1]:
                outputArray[j], outputArray[j + 1] = outputArray[j + 1], outputArray[j]


def arrayToString(arr): # конвертуємо кінцевий масив до типу string
    res = ""
    for i in arr:
        for j in i:
            res += str(j) + " "
        res += "\n"
    return res
