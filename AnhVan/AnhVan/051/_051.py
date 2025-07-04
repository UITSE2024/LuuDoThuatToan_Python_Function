def TichUocSo(nn):
    t = 1
    i = 1
    while i <= nn:
        if nn % i == 0:
            t = t * i
        i = i + 1
    return t

def main():
    n = int(input("Nhap n: "))
    print("Tich uoc so cua n:", TichUocSo(n))

if __name__ == "__main__":
    main()

