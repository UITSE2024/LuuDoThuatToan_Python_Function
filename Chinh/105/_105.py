def Tinh():
    s = 0
    m = 0
    e = 1
    i = 1
    while(e >= 10**(-6)):
        m += i
        e = 1/m
        s += e
        i += 1
    return s

def main():
    print("Ket qua: ", Tinh())

if __name__ == "__main__":
    main()
