import socket

def main():
	host = '192.168.43.232'  
	port = 8004

	s = socket.socket()
	s.connect((host,port))

	message = raw_input("-> ")
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		print "Linux : " + str(data)
		message = raw_input("-> ")
	s.close()

if __name__ == '__main__':
			main()		
