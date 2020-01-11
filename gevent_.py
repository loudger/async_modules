import gevent
from gevent.event import Event
from time import sleep, ctime

event = Event()


def simulation_work(time = 1):
	print('working time = ' + str(time))
	gevent.sleep(time) # Спит только этот поток
	print('done')
	event.set() # -> True

def loop():
	print('here')	
	# while True:  #Такой способ не работает
	# 	if event.is_set():
	# 		print(ctime)
	# 		event.clear()
	# 		break
	event.wait() #Блокирует поток, ждёт event
	print(ctime())

def main():
	threads = [gevent.spawn(simulation_work), gevent.spawn(loop)] #spawn() создаёт объект поток
	gevent.joinall(threads) #joinall() запускает все потоки в массиве

main()