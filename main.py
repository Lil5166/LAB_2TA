from inversion import inversion
from inversion import arraySort
from inversion import arrayToString
from inversion import inputFile
from inversion import inputArray
from inversion import outputArray
from inversion import index
from inversion import outputFile



def main(): # узагальнюємо код в одну функцію
    for row in inputFile:
        inputArray.append([int(i) for i in row.split()])
    for something in range(1, inputArray[0][0] + 1):
        if something == index:
            continue
        outputArray.append([something, inversion(something)])

    arraySort(outputArray)
    outputFile.write(arrayToString(outputArray))


if __name__ == '__main__': # виконуємо
    main()