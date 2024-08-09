x = "hello world"
print(x.capitalize()) # will convert first letter into capital

x1 = "HELLO WORLD"
print(x1.casefold()) # every thing into lower


x2 = "hyd"
print(x2.center(20))

x3 = "hello friends this is python class. All my friends are in the class friends"
print(x3.count("friends"))

x4 = "hello_"
print(x4.endswith("_"))

x5 = "hello friends this is python class. All my friends are in the class friends"
print(x5.find("f"))
print(x5.find("z"))

print(x5.index("f"))
# print(x5.index("z"))

x6 = "hello2"
print(x6.isalpha()) #it is used to check string is in alphabets or not

x7 = "hello233&"
print(x7.isalnum()) #to check alpha and numerical


x8 = "22332"
print(x8.isdecimal()) # is used to find the decimals 0 to 9

x9 = "\u00B2"
print(x9.isdigit())

x10 =  "de12"
print(x10.isidentifier()) # it was name given to variable

x11 = "helo"
print(x11.islower())
print(x11.isupper())

x12 = "     "
print(x12.isspace)

x13 = "   s  "
print(x13.isspace)

x14 ="hello my world my"
print(x14.replace("my", "sky"))

x15 = "$jhhw"
print(x15.startswith("$"))

x16 = " HELLO world"
print(x16.swapcase())

x17 = "22"
print(x17.zfill(10))
