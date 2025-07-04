def KtChinhPhuong(nn):
    flag = 0
    i = 0
    while(i <= nn):
        if(i * i == nn):
            flag = 1
        i += 1
    if(flag == 1):
        return True
    return False

def main():
	n = int(input("Nhap n: "))

	if(KtChinhPhuong(n)):
		print("La so chinh phuong")
	else: 
		print("Khong la so chinh phuong: ")

if __name__ == "__main__":
    main()