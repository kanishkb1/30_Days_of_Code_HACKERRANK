#step-1: set data
n=int(input())

#step-2: string manipulation
for i in range(0,n):
    s=input()
    print(s[0::2]+" "+s[1::2])
