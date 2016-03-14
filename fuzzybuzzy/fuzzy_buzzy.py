for x in range(1,100):
	if((x%3==0) and (x%5)!=0):
		print x,"-fuzzy"
	elif((x%5==0) and (x%3)!=0):
		print x,"-buzzy"
	elif((x%3==0) and (x%5)==0):
		print x,"-fuzzybuzzy"
	else:
		print(x)	