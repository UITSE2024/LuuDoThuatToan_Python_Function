from math import sqrt


def Nhap():
    a=int(input("Nhap a: "))
    b=int(input("Nhap b: "))
    c=int(input("Nhap c: "))
    return a,b,c
def Giaiphuongtrinh(a,b,c):
    delta=b*b-4*a*c
    if (delta<=0):
        if(delta==0):
            x=(-b)/2*a
            print("Mot ngiem:", x)
        else:
            print("Vo nghiem")
    else:
        x1=(-b+sqrt(delta))/2*a
        x2=(-b-sqrt(delta))/2*a
        print("Hai ngiem: ", x1, x2)
def main():
    a,b,c=Nhap()
    Giaiphuongtrinh(a,b,c)
if __name__ == "__main__":
    main()