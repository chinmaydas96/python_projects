# input the ip address of the server and give the range of port for scan
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server=input("enter the server name or address ")
if(server):
	def pscan(port):
		try:
			s.connect((server,port))
			return True
		except:
			return False
	fport=int(input("enter starting port  :"))		
	lport=int(input("enter last port      :"))
	for x in range(fport,lport):
		if pscan(x):
			print('port',x,'is open')
		else:
			print("port",x,"is closed")
else:
	raise Exception("please enter a valid server")