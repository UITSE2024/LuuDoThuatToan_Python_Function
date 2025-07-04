import sys

def Tinh(xx: int, nn: int) -> int:
    t = 1
    s = 0
    i = 1

    while i <= nn:
        t = t * xx
        s = s + t
        i = i + 1

    return s

def main() -> int:
    n = int(input("n = ") or 0)
    x = int(input("x = ") or 0)
    s = Tinh(x, n)
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())
