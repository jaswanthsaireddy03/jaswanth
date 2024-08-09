dict = {
    "name":"ram",
    "age":122,
    "city":"delhi",
    "subjects": [12,33,44,55,33,66,77],
    "address": {
        "rno" : 22,
        "street" : "nehru nagar",
        "city" : "hyderabad"
    }
}
print(dict)
print(len(dict))
print(type(dict))
print(dict["name"])
print(dict["age"])
print(dict["subjects"])
print(dict["subjects"][2])
print(dict["address"]["street"])
print(".....marks....")
print(len(dict["subjects"]))


for x in dict["subjects"]:
    print(x)


dict["age"] = 22
print(dict)