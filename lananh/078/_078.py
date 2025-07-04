def tinhs(xx, nn):
    s = 1
    t = 1
    i = 1
    while(i <= nn):
        t = t * xx
        s = s + t
        i = i + 1
    return s

def main():
    x = float(input("Nhap x :"))
    n = int(input("Nhap n: "))
    print("Tong s = ", tinhs(x, n))
if __name__ == "__main__":
    main()
