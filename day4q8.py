def RL(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    if (x == 'L'):
        return 50
    if (x == 'C'):
        return 100
    if (x == 'D'):
        return 500
    if (x == 'M'):
        return 1000
    return -1
def s(str):
    a = 0
    i = 0
    while (i < len(str)):
        x1 = RL(str[i])
        if (i + 1 < len(str)):
            x2 = RL(str[i + 1])
            if (x1 >= x2):
                a = a + x1
                i = i + 1
            else:
                a = a + x2 - x1
                i = i + 2
        else:
            a = a + x1
            i = i + 1
    return a
n=str(input("enter a roman num"))
print(s(n))
