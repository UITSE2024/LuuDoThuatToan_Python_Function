
def tinhPi():
    s = 3
    dau = 1
    e = 3
    i = 2
    epsilon = 1**-6
    while e >= epsilon:
        e = 4 / (i * (i + 1) * (i + 2))
        s += dau * e
        dau = -dau
        i += 2

    return s

def main():
    Pi = tinhPi();

    print("Gia tri cua pi: {:.4f}".format(Pi))

if __name__ == "__main__":
    main()



