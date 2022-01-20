def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manacher(string):
    string = UpdatedString(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0
 
    for i in range(len(string)):
        imir = 2 * C - i
        if R > i:
            LPS[i] = min(R-i, LPS[imir])
        else:
            LPS[i] = 0
 
        try:
            while string[i + 1 + LPS[i]] \
            == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
 
    r, c = max(LPS), LPS.index(max(LPS))
    return r
 
inp=str(input())
print(Manacher(inp))