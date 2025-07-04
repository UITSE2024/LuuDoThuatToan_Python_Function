def chuyenSangDoC(F):
    C = 5 / 9 * (F - 32)
    return C 

def main():
    F = float(input("Nhap vao do F: "))
    C = chuyenSangDoC(F)
    print("{} do C tuong ung {:.1f} do F".format(F, C))

if __name__ == "__main__":
    main()



