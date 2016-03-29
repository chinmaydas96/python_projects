import socket
import threading 
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print str(data)
		except:
			pass
		finally:
			tLock.releases()

host = "127.0.0.1"
port = "0"

server = '127.0.0.1'						