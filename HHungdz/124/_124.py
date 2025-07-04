def timSoHangThuN(nn):
    at = 2
    bt = 1
    for i in range(2, nn + 1):
        ahh = at * at + 2 * bt * bt
        bhh = 2 * at * bt
        at = ahh
        bt = bhh 

    return at, bt

def main():
    n = int(input("Nhap vao gia tri cua n: "))
    An, Bn = timSoHangThuN(n)

    print("So hang An = {}, Bn = {}".format(An, Bn))


if __name__ == "__main__":
    main()


