#   TO COUNT THE OCCURRENCES OF EACH WORD IN A GIVEN STRING

a=input('enter the string:')
l=a.split()
d={}
for i in l:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)