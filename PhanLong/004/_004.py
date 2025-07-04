import sys
from math import pi as M_PI

def TinhDienTichXungQuanh(rr: float) -> float:
    return 4 * M_PI * rr ** 2

def main() -> int:
    r = float(input("r = ") or 0)
    s = TinhDienTichXungQuanh(r);
    print(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())