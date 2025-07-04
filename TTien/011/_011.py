from math import sqrt

def Nhap():
    xx=float(input("Nhap hoanh do: "))
    yy=float(input("Nhap tung do: "))
    return xx, yy

def Xuat(xx, yy):
    print("Hoanh do: ", xx)
    print("Tung do: ", yy)

def DienTich(x1, y1, x2, y2, x3, y3):
    a = sqrt((x2-x1)**2 + (y2-y1)**2)
    b = sqrt((x2-x3)**2 + (y2-y3)**2)
    c = sqrt((x3-x1)**2 + (y3-y1)**2)
    p = (a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s

def main():
    print("Nhap diem thu nhat: ")
    x1, y1 = Nhap()
    print("Nhap diem thu hai: ")
    x2, y2 = Nhap()
    print("Nhap diem thu ba: ")
    x3, y3 = Nhap()

    print("Diem thu nhat: ")
    Xuat(x1, y1)
    print("Diem thu hai: ")
    Xuat(x2, y2)
    print("Diem thu ba: ")
    Xuat(x3, y3)
    print("Dien tich: ", DienTich(x1, y1, x2, y2, x3, y3))

if __name__ == "__main__":
    main()





