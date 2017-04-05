import GDAX

class MyWebsocketClient(GDAX.WebsocketClient):
        def __init__(self):
            super(MyWebsocketClient, self).__init__()
            self.stop = False

        def onOpen(self):
            print("-- Connection Initiated --")

        def onMessage(self, msg):
            if msg["type"] == "match":
                print(float(msg["price"]))
            #print("Message type: ", msg["type"], "\t@ %.3f" % float(msg["price"]))
            #print(msg)

        def onClose(self):
            print("-- Connection Closed --")



