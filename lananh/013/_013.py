
import math 

def tinhx7(xx):
    x2 = xx * xx
    x4 = x2 * x2
    x8 = x4 * x4
    x7 = x8 / xx
    return x7

def main():
    x = float (input("Nhap x: "))
    print ("x^7 = ", tinhx7(x))
    return 0

if __name__ == "__main__":
    main()
