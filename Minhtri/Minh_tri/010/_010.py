from math import sqrt

def Nhap():
    xx=int(input("Nhap hoanh do: "))
    yy=int(input("Nhap tung do: "))
    return xx, yy

def Xuat():
    print("Hoanh do:", xx)
    print("Tung do:", yy)

def Khoangcach(x1, x2, y1, y2):
    return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

def Chuvi(a, b, c):
    return a+b+c

def main():
    print("Diem thu nhat: ")
    x1, y1 = Nhap()
    print("Diem thu hai: ")
    x2, y2 = Nhap()
    print("Diem thu ba: ")
    x3, y3 = Nhap()
    a=Khoangcach(x2,y2,x3,y3)
    b=Khoangcach(x1,y1,x3,y3)
    c=Khoangcach(x1,y1,x2,y2)
    print("Chu vi: ", Chuvi(a,b,c))

if __name__=="__main__":
    main()


