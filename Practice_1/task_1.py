"""
Дано число n. С начала суток прошло n минут. Определите, сколько
часов и минут будут показывать электронные часы в
этот момент. Программа должна вывести два числа:
количество часов (от 0 до 23) и количество минут (от 0 до 59).
Учтите, что число n может быть больше, чем количество минут в сутках.
"""

time = input()
cloc=int(time)//60
min=int(time)%60
if cloc< 24:
    print(cloc)
    print(min)
else:
    print(cloc%24)
    print(min)
