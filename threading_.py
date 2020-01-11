import threading
from time import sleep, ctime

e = threading.Event()
e.clear() # -> False

def simulation_work(time = 1):
	print('working time = ' + str(time))
	sleep(time)

def loop():
	e.wait()
	while e.is_set(): #Это не обязательно
		print(ctime)
		e.clear()

def main():
	thread = threading.Thread(target = loop)
	thread.start()

	simulation_work(2)
	e.set()

main()