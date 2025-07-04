def sohangthuN(nn):
    if(nn==1):
        return 1,1
    else:
        at=1
        bt=1
        i=2
        while i <= nn:
            a = 3*bt + 2*at
            b = 3*bt + at
            i += 1
            at=a
            bt=b
        return at, bt



def main():
    n = int(input("Nhap n: "))
    a, b = sohangthuN(n)
    print("a(n) =", a)
    print("b(n) =", b)

if __name__ == "__main__":
    main()



