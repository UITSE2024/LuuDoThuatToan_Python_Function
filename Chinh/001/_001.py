from math import sqrt

def Nhap():
    xx = float(input("Nhap hoanh do: "))
    yy = float(input("Nhap tung do: "))
    return xx, yy;

def Xuat(xx, yy):
    print("Hoanh do: ", xx)
    print("Tung do: ", yy)

def KhoangCach(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    print("Diem thu nhat: ")
    x1, y1 = Nhap()
    print("Diem thu hai: ")
    x2, y2 = Nhap()
    print("Khoang cach: ", KhoangCach(x1, y1, x2,y2))

if __name__ == "__main__":
    main()
