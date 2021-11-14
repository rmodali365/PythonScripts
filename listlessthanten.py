def listLessThanNum(list,num):
    newList = []
    for x in list:
        if x<num:
            newList.append(x)
    print(newList)

num1 = int(input('choose a number: '))
list = [1,2,3,4,5,345,67,86]
listLessThanNum(list,num1)

