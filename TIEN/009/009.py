from math import pi,sin

def Nhap():
    n = int(input())
    r = float(input())
    return n, r
def DienTich(r, n):
    return n*r*r*sin(2*pi/n)/2
def main():
    n, r = Nhap()
    print(DienTich(r, n))
if __name__ == "__main__":
    main()