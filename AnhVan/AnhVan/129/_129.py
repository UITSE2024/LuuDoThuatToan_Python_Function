def XepTang(aa, bb, cc):
    if aa > bb:
        temp = aa
        aa = bb
        bb = temp
    if aa > cc:
        temp = aa
        aa = cc
        cc = temp
    if bb > cc:
        temp = bb
        bb = cc
        cc = temp
    return aa, bb, cc

def Xuat(aa, bb, cc):
    print("a =", aa)
    print("b =", bb)
    print("c =", cc)

def main():
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    c = float(input("Nhap c: "))
    print("Truoc khi xep tang:")
    Xuat(a,b,c)

    print("Sau khi xep tang:")
    a, b, c = XepTang(a,b,c)
    Xuat(a,b,c)

if __name__ == "__main__":
    main()

