
#GitHub Example
import random

def sortKey(k):
    return k[1]

myList = []

for i in range (0,100):
    myList += [[random.randint(1,100), chr(random.randint(65,90))]]

#myList.sort()
myList.sort(key=sortKey)

for n in myList:
    print(n)

