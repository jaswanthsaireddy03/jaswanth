list = [1,2,3,4,5,6,7,8,9,10,11]
n = len(list)
# for x in range(0,n,2): # for odd numbers
#     list [x] = list[x] + 100
# print(list)
for x in range(1,n-1,2):
    list[x] = list[x] +100 # for even numbers
print(list)