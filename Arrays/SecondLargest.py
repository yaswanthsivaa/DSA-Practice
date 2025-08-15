# SecondLargest Element in the List

def linearSearch(listOfNumbers):
    for i in listOfNumbers:
      maxNum = max(listOfNumbers)
      secondLargeNum = None
      for j in listOfNumbers:
          if j == maxNum:
              continue
          else:
              if j > i:
                 secondLarge = j
    return secondLarge

def secondLargestElement(listOfNumbers):
    return linearSearch(listOfNumbers)


num = input('Enter the numbers :').split(',')

SL = secondLargestElement(num)

print(f"second Largest in the Array is :{SL}")




