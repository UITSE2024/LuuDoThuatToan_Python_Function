def Nhap():
    a = int(input())
    b = int(input())
    return a, b

def GiaTriLonNhat(aa, bb):
    lc = aa
    if(lc > bb): return lc
    return bb
def main():
    a, b = Nhap()
    print(GiaTriLonNhat(a, b))
if __name__ == "__main__":
    main()