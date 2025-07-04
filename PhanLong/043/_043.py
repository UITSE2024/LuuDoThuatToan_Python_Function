import sys

def Tinh(nn: int) -> float:
    s = 0
    i = 1

    while i <= nn:
        s = s + 1 / (i * (i + 1) * (i + 2))
        i = i + 1

    return s

def main() -> int:
    n = int(input("n = ") or 0)
    s = Tinh(n)
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())