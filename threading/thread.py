from threading import Thread
import time


def timer(name, delay, repeat):
	print "Timer: " + "name" + "Started"
	while repeat > 0:
		time.sleep(delay)
		print name + ":" + str(time.ctime(time.time()))
		repeat -= 1
	print "Timer: " + name + "Completed"


def main():
		t1 = Thread(target=timer, args=("Timer",1,5))
		t2 = Thread(target=timer, args=("Timer",2,5))
		t1.start()
		t1.start()

		print "main Completed"

if __name__ == '__main__':
		main()	