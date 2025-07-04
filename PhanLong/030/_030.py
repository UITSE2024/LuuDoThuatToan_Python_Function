import sys

def Tinh(nn: int) -> float:
    s = 0
    i = 2
    while i <= 2 * nn:
        s = s + 1 / i
        i = i + 2
    return s

def main() -> int:
    n = int(input("n = ") or 0)
    s = Tinh(n)
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())