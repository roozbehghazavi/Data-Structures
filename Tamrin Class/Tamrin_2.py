s=str(input("Please Enter The String:"))

def Duplicate(s):
    if(len(s)==0):
        return True
    if(s[:int(len(s)/2)]!=s[int(len(s)/2):]):
        return False

    else:
        s1=s[1:int(len(s)/2)]
        s2=s[int(len(s)/2)+1:]
        if(s1==s2):
            return (Duplicate(s1))

print(Duplicate(s))