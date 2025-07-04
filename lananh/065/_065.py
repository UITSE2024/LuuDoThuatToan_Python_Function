def chusonhonhat(nn):
    lc = nn % 10
    t = nn
    while (t != 0):
        dv = t % 10
        if (dv < lc):
            lc = dv
        t = t // 10
    return lc
def main():
    n = int(input("Nhap n: "))
    print("Chu so nho nhat cua n: ", chusonhonhat(n))

if __name__ == "__main__":
    main()
