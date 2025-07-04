def tinh_pi_bbp(epsilon=1e-6):
    s = 4 - 2/4 - 1/5 - 1/6
    t = 1
    e = 1
    i = 1

    while e >= epsilon:
        t = t * 16
        term1 = (4 / (8 * i + 1))
        term2 = (2 / (8 * i + 4))
        term3 = (1 / (8 * i + 5))
        term4 = (1 / (8 * i + 6))
        e = (term1 - term2 - term3 - term4) / t
        s = s + e
        i = i + 1

    return s

def main():
    pi_value = tinh_pi_bbp()
    print(f"Gia tri cua pi: {pi_value:.6f}")

if __name__ == "__main__":
    main()