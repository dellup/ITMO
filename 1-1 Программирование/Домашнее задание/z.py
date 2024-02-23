a, b, c, d = input().split()
if b == d:
	new1 = a + c
	flag = True
	while flag:
		for i in range(2, min(new1, b)+1):
			if (new1%i==0 and b%i==0):
				new1 //= i
				b //= i
				break
		else:
			flag = False
	print(new1, b)
else:
	new2 = b*d
	new1 = (a*d + c*b)
	flag = True
	while flag:
		for i in range(2, min(new1, new2)+1):
			if (new1%i==0 and b%i==0):
				new1 //= i
				new2 //= i
				break
		else:
			flag = False
	print(new1, new2)