import math

def tinhChuVi(nn, rr):
    return 2 * nn * rr * math.sin(math.pi / nn)

def main():
    n = int(input("Nhap so canh cua da giac deu: "))
    r = float(input("Nhap ban kinh cua duong tron ngoai tiep: "))
    
    chu_vi = tinhChuVi(n, r)
    print(f"Chu vi cua da giac deu la: {chu_vi:.2f}")

if __name__ == "__main__":
    main()
