import math
def TongLuyThua(nn, kk):
    s = 0
    i = 1
    while i <= nn:
        s = s + math.pow(i, kk)
        i = i + 1
    return s

def main():
    k = int(input("Nhap k: "))
    n = int(input("Nhap n: "))
    print("S(n,k) =", TongLuyThua(n,k))

if __name__ == "__main__":
    main()

