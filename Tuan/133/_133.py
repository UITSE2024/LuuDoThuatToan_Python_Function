def Nhap():
    xx = int(input("Nhap x = "))
    yy = int(input("Nhap y = "))
    zz = int(input("Nhap z = "))
    return xx, yy, zz

def plTamGiac(xx, yy, zz):
    if xx + yy > zz and yy + zz > xx and xx + zz > yy:
        if xx == yy and yy == zz:
            print("Deu")
        else:
            if xx ** 2 == yy ** 2 + zz ** 2 or yy ** 2 == xx ** 2 + zz ** 2 or zz ** 2 == xx ** 2 + yy ** 2:
                if xx == yy or yy == zz or zz == xx:
                    print("Vuong can")
                else:
                    print("Vuong")
            else:
                if xx == yy or yy == zz or zz == xx:
                    print("Can")
                else:
                    print("Nhon")
    else:
        print("Ko")

def main():
    x, y, z = Nhap()
    plTamGiac(x, y, z)

if __name__ == "__main__":
    main()