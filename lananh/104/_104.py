def tinhs():
    s = 0
    e = 0.5
    i = 1
    while(e >= 10**-6):
        e = 1 / (i * (i + 1))
        s = s + e
        i = i + 1
    return s

def main():
    print("Tong s = ", tinhs())

if __name__ == "__main__":
    main()
