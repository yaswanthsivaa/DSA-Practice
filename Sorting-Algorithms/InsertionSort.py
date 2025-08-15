# Insertion Sort

def insertionSort(numbersList, size):
    
    for i in range(1, size):
        for j in range(1,size):
            previous = j - 1
            currentElement = numbersList[j]
            
            while previous > -1 and numbersList[previous] > currentElement:
                numbersList[previous+1] = numbersList[previous]
                previous -= 1
            
            numbersList[previous+1] = currentElement

numbers = []

size = int(input('Enter the List size :'))
for i in range(size):
    num = int(input('Enter the number :'))
    numbers.append(num)

insertionSort(numbers, size)

print(numbers)



