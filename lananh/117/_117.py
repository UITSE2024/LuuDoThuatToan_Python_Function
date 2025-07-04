def tinh(nn):
    att = -1
    at = 3
    t = 2
    i = 2
    while(i <= nn):
        t = t * 2
        ahh = 5 * t + 5 * at - att
        i += 1
        att = at
        at = ahh
    return ahh

def main():
    n = int(input("Nhap n:"))
    print("So hang thu n: ", tinh(n))

if __name__ == "__main__":
    main()
