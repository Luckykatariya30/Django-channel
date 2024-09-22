from channels.consumer import SyncConsumer , AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import json
from asgiref.sync import async_to_sync
from .models import Chat,Group



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocet Connected...',event)
        self.send({
            'type':'websocket.accept'
        })
        
    # def websocket_receive(self,event):
    #     print('Websocet Receive...' ,event['text'])
    #     for i in range(5):
    #         self.send({
    #             'type':'websocket.send',
    #             'text':str(i),
    #         })
    #         sleep(2)
    
    
# DICTIONARY RETURN .....


    def websocket_receive(self,event):
        print('Websocet Receive...' ,event['text'])
        for i in range(5):
            self.send({
                'type':'websocket.send',
                'text':json.dumps({'count':i}),
            })
            sleep(2)
        
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




# CHAT APP CONSUMER ........

class ChatAppSyncConsumer(SyncConsumer):
    

    def websocket_connect(self,event):
        print('this client site send message....', event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Name...',self.channel_name)
        
        # dynamic group ka name

        self.group_name = self.scope['url_route']['kwargs']['group_ka_name']
        print('Group Name : ',self.group_name)
        
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.send({
            
            'type':'websocket.accept',
        })
        
    def websocket_receive(self,event):
        print('this is client site to recieve message...',event['text'])
        print('type of event[text]',type(event['text']))
        
        
## SAVE CHATS IN DATABASE ###################
    
        group = Group.objects.get(group_name=self.group_name)
        print('event....', event)
        print('event....', event['text'])
        print('type of event....', type(event))
        print('type of event[text]....',type(event['text']))
        
        data = json.loads(event['text'])
        actual_data= data['meg']
        print('thsi is actual message.....',actual_data)
        chat = Chat(group_name = group , contant = actual_data)
        chat.save()
        

        ## MESSAGE SEND  IN  GROUP ...........
        
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self,event):
        print('event ....',event['message'])        
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })
        
    def websocket_disconnect(self,event):
        print('this client is disconnect message...',event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Name...',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        raise StopConsumer()