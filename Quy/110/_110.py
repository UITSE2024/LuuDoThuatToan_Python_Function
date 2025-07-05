def Tinh():
    s = 0
    dau = 1
    e = 4
    i = 1
    epsilon = 10 ** -6
    while (e >= epsilon):
        e = 4 / i
        s = s + dau * e
        i = i + 2
        dau = -1 * dau
    return s

def main():
    print("Pi: ", Tinh())

if __name__ == "__main__":
    main()