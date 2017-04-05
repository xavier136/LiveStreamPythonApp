from MySocketClient import MyWebsocketClient
import time

wsClient = MyWebsocketClient()

wsClient.start()
    # Do some logic with the data
while not (wsClient.stop) :
    time.sleep(10)
wsClient.close()
