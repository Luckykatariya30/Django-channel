from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocet Connected...',event)
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self,event):
        print('Websocet Receive...' ,event['text'])
        self.send({
            'type':'websocket.send',
            'text':'this is a server site message',
        })
        
    def websocket_desconnect(self,event):
        print('Websocet Disconnected...' ,event)
        raise StopConsumer()
        
 


        
#  Async Consumer ...

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('Websocet Connected...' ,event)
        await self.send({
            'type':'websocket.accept',
        })
        
    async def websocket_receive(self,event):
        print('Websocet Receive...' ,event)    
        
    async def websocket_desconnect(self,event):
        print('Websocet Disconnected...' ,event)
        raise StopConsumer()
    