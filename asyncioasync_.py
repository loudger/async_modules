import asyncio
from time import sleep, ctime

def simulation_work(time = 1):
	print('working time = ' + str(time))
	sleep(time)

async def loop_func(event):
	await event.wait() # блокирует поток, ждёт event
	print('loop_func')
	sleep(1)
	print('ctime')

async def main():
	# thread = asyncio.async(loop()) # Один из способов создать поток
	# thread.start() # И запустить этот поток

	event = asyncio.Event()
	waiter_task = asyncio.create_task(loop_func(event))

	simulation_work(1)
	print('done')
	event.set()
	# asyncio.sleep(1)
	# loop = asyncio.get_event_loop()
	# loop.run_until_complete(loop_func())
	# await waiter_task
	print('here')


asyncio.run(main())