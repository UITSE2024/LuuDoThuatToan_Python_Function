import sys

def TinhX11(xx: float) -> float:
    x2 = xx * xx
    x4 = x2 * x2
    x8 = x4 * x4
    x10 = x8 * x2
    x11 = x10 * x
    return x11

def main() -> int:
    x = float(input("x = ") or 0)
    x11 = TinhX11(x)
    print(x11)
    return 0

if __name__ == "__main__":
    sys.exit(main())