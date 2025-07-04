import sys
from math import sqrt

def Tinh(nn: int) -> float:
    s = 0.0
    i = nn
    
    while i > 0:
        s = sqrt(i + s)
        i = i - 1

    return s

def main() -> int:
    n = int(input("n = ") or 0)
    s = Tinh(n)
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())