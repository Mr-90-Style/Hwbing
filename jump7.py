i=0
while 1 :
	if i==100:
		break
	i += 1
	if i % 7 == 0 :
		print(i)
	elif i // 7 ==0 and i > 7:
		print(i)
	elif i - ((i // 10) * 10) == 7:
		print(i)
	elif i // 10 == 7:
		print(i)

