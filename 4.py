#  TO REVERSE THE STRING

def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s="helloworld"
print("original string is:",end="")
print(s)
print("reverse string is:",end="")
print(reverse(s))