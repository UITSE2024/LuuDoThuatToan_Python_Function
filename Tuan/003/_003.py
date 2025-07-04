from math import pi

def Nhap():
    rr = int(input("Nhap r = "))
    return rr

def Tinh(rr):
    p = 2 * pi * rr
    return p

def main():
    r = Nhap()
    print("Chu vi duong tron:", Tinh(r))

if __name__ == "__main__":
    main()