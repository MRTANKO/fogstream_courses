v=int(input())
t=int(input())
s=v*t
if 0<=s<109:
    print(s)
elif s>=109 or s<-109:
    print(s%109)
elif -109<=s<0:
    print(109+s)
