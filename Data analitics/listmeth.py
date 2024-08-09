list = [11,22,333,44,55]
list.append(1111111)
print(list)

list.clear()
print(list)

list2 = ["raj", "ravi", 123 ]
l3 = list2.copy()
print(l3)

list3 = [1,1,1,1,2,3,4,4,554,3]
print(list3.count(1))

list4 = [ "hari", "ram"]
list3.extend(list4)
print(list3)
print(list3.index(3))
list3.insert(5,"raj")
list3.insert(0,0000)
print(list3)
list3.pop()
list3.pop()
list3.pop(0)
print(list3)