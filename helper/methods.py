import random
def generateArray(n,min,max):
    arr=[]
    for i in range(n):
        Y = random.randint(min,max)
        arr.append(Y)
    return arr