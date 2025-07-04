from math import sqrt

def Nhap():
	x1 = int(input("Nhap x1: "))
	y1 = int(input("Nhap y1: "))
	x2 = int(input("Nhap x2: "))
	y2 = int(input("Nhap y2: "))
	x3 = int(input("Nhap x3: "))
	y3 = int(input("Nhap y3: "))
	return x1, y1, x2, y2, x3, y3;

def KtTamGiac(xx1, yy1, xx2, yy2, xx3, yy3):
	a = sqrt((xx2 - xx1) * (xx2 - xx1) + (yy2 - yy1) * (yy2 - yy1));
	b = sqrt((xx3 - xx1) * (xx3 - xx1) + (yy3 - yy1) * (yy3 - yy1));
	c = sqrt((xx3 - xx2) * (xx3 - xx2) + (yy3 - yy2) * (yy3 - yy2));
	if (a + b > c and a + c > b and b + c > a):
		return True;
	else:
		return False;

def main():
	x1, y1, x2, y2, x3, y3 = Nhap()

	if(KtTamGiac(x1, y1, x2, y2, x3, y3)):
		print("La tam giac.")
	else: 
		print("Khong la tam giac: ")

if __name__ == "__main__":
    main()

