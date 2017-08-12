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
