from math import pi,sin

def Nhap():
    n = int(input())
    r = float(input())
    return n, r
def DienTich(rr, nn):
    return nn*rr*rr*sin(2*pi/nn)/2
def main():
    n, r = Nhap()
    print(DienTich(r, n))
if __name__ == "__main__":
    main()