import socket

def main():

	host = '127.0.0.1'
	port = 8004

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print("Window : " + str(addr))
	while True:
		data = c.recv(1024)
		if not data:
			break
		print("Server : " + data.decode("utf-8"))
		#data = str(data).upper()
		data = input("-> ")
		c.send(bytes(data, 'utf-8'))
	c.close()
	
if __name__ == '__main__':
	main()		 
