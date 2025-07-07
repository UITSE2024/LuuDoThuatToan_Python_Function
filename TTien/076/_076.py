
def Tinh(nn, xx):
    s = 1 + xx
    t = xx
    m = 1
    i = 3
    while(i<=2*nn+1):
        t = t * xx * xx
        m = m*i*(i-1)
        s = s + t/m
        i = i + 2
    return s 

def main():
    n = int(input("Nhap n: "))
    x = float(input("Nhap x: "))
    print(Tinh(n, x))

if __name__=="__main__":
    main()