import sys

def Fibonacci(nn: int) -> int:
    att = 1
    at = 1
    i = 2
    ahh = 1

    while i <= nn:
        ahh = at + att
        i = i + 1
        att = at
        at = ahh

    return ahh

def main() -> int:
    n = int(input("n = ") or 0)
    ahh = Fibonacci(n)
    print(ahh)
    return 0

if __name__ == "__main__":
    sys.exit(main())
