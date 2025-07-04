import sys

def KiemTraBatDangThuc(xx: int, yy: int, zz: int) -> bool:
    if xx <= yy <= zz:
        return True
    else:
        return False

def main() -> int:
    x = int(input("x = ") or 0)
    y = int(input("y = ") or 0)
    z = int(input("z = ") or 0)

    if KiemTraBatDangThuc(x, y, z):
        print("Bat dang thuc dung")
    else:
        print("Bat dang thuc khong dung")

    return 0

if __name__ == "__main__":
    sys.exit(main())
