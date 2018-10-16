time = input()
cloc=int(time)//60
min=int(time)%60
if cloc< 24:
    print(cloc)
    print(min)
else:
    print(cloc%24)
    print(min)
