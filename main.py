from queue import Queue
from threading import Thread
from chatbot import chatbot
from chatInterface import runInterface


# Create the shared queue and launch both threads
global que
que = Queue()

t1 = Thread(target = runInterface, args =(que, ))
t2 = Thread(target = chatbot, args =(que, ))
t1.start()
t2.start()
  
# Wait for all produced items to be consumed
que.join()
