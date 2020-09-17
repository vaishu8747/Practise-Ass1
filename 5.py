# TO CHECH WETHER GIVEN STRING IS PALINDROME OR NOT

def Palindrome(s):
    return s==s[::-1]
s="malayalam"
ans=Palindrome(s)
if ans:
    print("Yes")
else:
    print("No")