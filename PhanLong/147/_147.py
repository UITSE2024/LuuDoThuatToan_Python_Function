import sys

def KiemTraToanLe(nn: int) -> bool:
    flag = 1
    t = nn

    while t != 0:
        dv = t % 10
        if dv % 2 == 0:
            flag = 0
        t = t / 10

    if flag == 1:
        return True
    else:
        return False

def main() -> int:
    n = int(input("n = ") or 0)

    if KiemTraToanLe(n):
        print("Toan le")
    else:
        print("Khong toan le")

    return 0

if __name__ == "__main__":
    sys.exit(main())