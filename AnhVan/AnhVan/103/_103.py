def Tinh(ss):
    e = 1
    i = 1
    ep = 10e-6
    while e >= ep:
        e = 1/i
        ss = ss + e
        i = i + 2
    return ss

def main():
    s = 0
    print("S(n) =", Tinh(s))

if __name__ == "__main__":
    main()
