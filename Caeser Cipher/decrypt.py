code=input("enter the coded text")
distance=int(input("enter the distance value"))
plaintext=""
for ch in code:
	ordvalue=ord(ch)
	ciphervalue=ordvalue-distance
	if ciphervalue < ord('a'):
		ciphervalue=ord('z') -(distance-(ord('a')-ordvalue + 1))
	plaintext+=chr(ciphervalue)
print(plaintext)					