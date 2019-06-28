# SET82
i=input()
e=0
k=['a','e','i','o','u','A','E','I','O','U']
for x in i:
    if any(char in k for char in i):
        e=1
        print('yes')
        break
    else:
        e+=1
if e!=1:

    print('no')
