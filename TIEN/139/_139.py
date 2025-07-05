
def Nhap():
    a = int(input())
    b = int(input())
    return a, b
def check(aa, bb):
    if(aa == 0):
        if(bb == 0):
            return 0
        return -1
    else:
        return 1
def GiaiPhuongTrinh(aa, bb):
    C = check(aa, bb)
    if(C == 0): print("VSN")
    elif(C == -1): print("VN")
    else: print((-bb)/aa)
def main():
    a, b = Nhap()
    GiaiPhuongTrinh(a,b)
if __name__ == "__main__":
    main()