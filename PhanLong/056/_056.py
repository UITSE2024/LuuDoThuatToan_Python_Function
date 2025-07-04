import sys

def DemSoUocChan(nn: int) -> int:
    dem = 0
    i = 2
    
    while i <= nn:
        if nn % i == 0:
            dem = dem + 1
        i = i + 2

    return dem

def main() -> int:
    n = int(input("n = ") or 0)
    dem = DemSoUocChan(n)
    print(dem)
    return 0

if __name__ == "__main__":
    sys.exit(main())
