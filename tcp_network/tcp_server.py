import socket


def main():

	host = '192.168.1.121'
	port = 8000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print "Window : " + str(addr)
	while True:
		data = c.recv(1024)
		if not data:
			break
		print "Window: " + str(data)
		#data = str(data).upper()
		data = raw_input("-> ")
		c.send(data)
	c.close()
	
if __name__ == '__main__':
		 	main()		 
