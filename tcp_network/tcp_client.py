import socket

def main():
	host = '127.0.0.1'  
	port = 8004

	s = socket.socket()
	s.connect((host,port))

	message = input("-> ")
	while message != 'q':
		s.send(bytes(message, 'utf-8'))
		data = s.recv(1024)
		print ("Client : " + data.decode("utf-8"))
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	main()		
