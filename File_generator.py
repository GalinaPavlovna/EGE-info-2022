from random import randrange
n=[[],[],[]]
n[0]='1234567890'
n[1]='qwertyuiopasdfghjklzxcvbnm'
n[2]=n[1].upper()

with open("file1.txt",'w') as f:
    for j in range(50):
        print("".join([n[0][randrange(len(n[0]))] for i in range(randrange(1,20))]),file=f)