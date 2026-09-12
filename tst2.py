list1= [5,2,8,1,3]
for i in range(5):
    for j in range(4):
        if list1[j] > list1[j + 1]:
            a= list1 [j]
            list1[j] = list1 [j + 1]
            list1[j + 1] = a
            print(list1)