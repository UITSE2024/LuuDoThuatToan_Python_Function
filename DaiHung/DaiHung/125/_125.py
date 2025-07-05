def Nhap():
    aa = int(input("Nhap a: "))
    bb = int(input("Nhap b: "))

    return aa, bb

def LayTriTuyetDoi(aa, bb):
    if aa < 0:
        aa = -aa
    if bb < 0:
        bb = -bb
    return aa, bb

def Xuat(aa, bb):
    print(f"a = {aa}, b = {bb}")

def main():
    a, b = Nhap()
    print("a va b truoc khi lay tri tuyet doi:")
    Xuat(a, b)
    a, b = LayTriTuyetDoi(a, b)
    print("a va b sau khi lay tri tuyet doi:")
    Xuat(a, b)


if __name__ == "__main__":
    main()