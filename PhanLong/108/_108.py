import sys

def TinhEX(xx: int) -> float:
    epsilon = 1e-6
    e = 1.0
    s = 1.0
    t = 1
    m = 1
    i = 1

    while e >= epsilon:
        t = t * xx
        m = m * i
        e = t / m
        s = s + e
        i = i + 1

    return s

def main() -> int:
    x = int(input("x = ") or 0)
    ex = TinhEX(x)
    print(ex)
    return 0

if __name__ == "__main__":
    sys.exit(main())