plaintext=input("enter one-word:\t")
distance=int(input("enter the distance value:"))
code=""
for ch in plaintext:
	ordvalue=ord(ch)
	ciphervalue=ordvalue+distance
	if ciphervalue > ord('z'):
		ciphervalue=ord('a')+distance -	(ord('z')-ordvalue + 1)
	code+= chr(ciphervalue)				
print (code)
