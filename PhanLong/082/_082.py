import sys
from math import sin

def Tinh(xx: int, nn: int) -> float:
    s = 0.0
    t = 1.0
    i = 1

    while i <= nn:
        t = t * sin(xx)
        s = s + t
        i = i + 1

    return s

def main() -> int:
    x = int(input("x = ") or 0)
    n = int(input("x = ") or 0)
    s = Tinh(x, n)
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())