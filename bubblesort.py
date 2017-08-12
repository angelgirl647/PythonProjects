# sorts numbers using bubble sorting! main goal is to get the largest number at the end of the list each time you loop through it


j=0
i=0
biggerNum=""
# var that measures length of list1, subtract 1 from the length of the list so the last number doesnt compare itself to an empty number
length=len(list1)-1

mylist = [54,34,45,23,88,98,37]

while j > -1:
    for i in range(0,length):
        if mylist[i+1] < mylist[i]:
            biggerNum = mylist[i]
            mylist[i] = mylist[i+1]
            mylist[i+1] = biggerNum
            print(myList)
            j +=1
        else:
            j -= 1


  
