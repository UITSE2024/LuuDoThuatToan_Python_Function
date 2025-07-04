def ktTamGiac(xx, yy, zz):
    if (xx + yy > zz and xx + zz > yy
        and yy + zz > xx):
        return True
    return False

def main():
    x = float(input("Nhap x:"))
    y = float(input("Nhap y:"))
    z = float(input("Nhap z:"))
    kt = ktTamGiac(x, y, z)
    if (kt == True):
        print("La tam giac")
    else:
        print("Khong la tam giac")

if __name__ == "__main__":
    main()
