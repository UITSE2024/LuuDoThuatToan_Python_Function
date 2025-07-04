def tinhs(nn):
    t = 1
    i = 1
    while(i <= nn):
        t = t * (1 + 1 / (i * i))
        i = i + 1
    return t

def main():
    n = int(input("Nhap n:"))
    print("Tong s = ", tinhs(n))

if __name__ == "__main__":
    main()