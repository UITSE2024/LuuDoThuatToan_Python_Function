def tinhs(xx, nn):
    s = -1
    t = 1
    m = 1
    i = 2
    dau = 1
    while(i <= 2 * nn):
        t = t * xx * xx
        m = m * i * (i - 1)
        s = s + dau * t / m
        i = i + 2
        dau = - dau
    return s
def main():
    x = float(input("Nhap x: "))
    n = int(input("Nhap n:"))
    print("Tong s = ", tinhs(x, n))
if __name__ == "__main__":
    main()