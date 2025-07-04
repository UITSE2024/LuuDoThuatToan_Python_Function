def Tinh(xx, nn):
    s = 1 - xx
    t = xx
    m = 1
    i = 3
    dau = 1
    while(i <= 2 * nn + 1):
        t *= xx * xx;
        m *= i * (i - 1)
        s += dau * t/m
        i += 2
        dau = -dau
    return s

def main():
    n = int(input("Nhap n: "))
    x = int(input("Nhap x: "))
    
    print("Ket qua: ", Tinh(x, n))

if __name__ == "__main__":
    main()