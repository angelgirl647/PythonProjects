# sorts numbers using bubble sorting! main goal is to get the largest number at the end of the list each time you loop through it
#
# place=""
# j=0
# i=0
# list1=[5,4,3,2,1]
# # var that measures length of list1, subtract 1 from the length of the list so the last number doesnt compare itself to an empty number
# length=len(list1)-1
#
# def swapNums():
#     for j in range(length):
#         for i in range(length):
#             if list1[i+1]<list1[i]:
#                 place=list1[i]
#                 list1[i]=list1[i+1]
#                 print(list1)
#                 list1[i+1]=place
#                 print(list1)
#                 i+=1
#             else:
#                 print("The list is sorted! :D")
#
# swapNums()

# list1=[5,4,3,2,1,9,8]
# i=0
# j=0
# n=len(list1)
#
# def numbers():
#     for j in range(n-1):
#         for i in range(n-1):
#             if list1[i] > list1[i+1]:
#                 list1[i],list1[i+1]=list1[i+1],list1[i]
#                 print(list1)
#
#
# numbers()

list2=[1,2,3,4,5,6]
print(list2)

end = list2[len(list2)-1]
start = list2[0]

value=int(input("Give me a numero"))

run=True
found = False
while run:
    midnum= (start + end)/ 2
    if value > midnum:
        start = midnum
        if value>end:
            print("no such num")
            break
        else:
            continue

    elif value<midnum:
        end=midnum
        if value<start:
            print("no such num")
            break
        else:
            continue

    else:
        found = True
        print("We found your num")
        break
