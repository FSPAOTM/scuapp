# chat/consumers.py
from turtle import pd

from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.layers import get_channel_layer
from wechat.models import Tbquery
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    users = [] #存储在线列表，所有用户共享的变量
    async def connect(self):
        # 获取用户名
        user_name = self.scope['url_route']['kwargs']['user_name']
        #添加进在线用户列表。添加之前，可以做一系列操作，例如查看用户是否合法访问等
        self.users.append({'user_name':user_name,'channel_name':self.channel_name})
        # 同意连接
        await self.accept()
        print(user_name)

        #检查是否有历史未读消息，若有，则发送给用户(还可以从数据库读取）
        # message = []
        # filterresult = Tbquery.objects.filter(To_name=user_name)
        # #print(filterresult)
        # if len(filterresult)>0:
        #      for item in filterresult:
        #          #如果历史消息里这条记录是发送给刚登录的用户的，添加进用户历史信息列表
        #          if item.Isread==0:
        #              message.append(item.q_content)
        # # 如果message长度大于零，表示有历史记录，缺少逻辑匹配对方id
        # if len(message)>0:
        #      # for item in message:
        #      #     self.history.remove(item)
        #      print(self.channel_name)
        #      await self.send(
        #          text_data=json.dumps({
        #              'message': message
        #          }))
        #      print("发送成功")
        #      for item in filterresult:
        #          item.Isread = 1
        #          Tbquery.objects.update(Isread=item.Isread)





    async def disconnect(self, close_code):
        #从在线列表中移除后退出
        self.users.remove({'user_name':self.scope['url_route']['kwargs']['user_name'],'channel_name':self.channel_name})
        await self.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # 往特定channel发消息，这边是写死的，前端传过来的To_ID是test01
        to = text_data_json['to']

        # 若已经登录，则直接发送
        channel_name = ''
        for item in self.users:
            if item['user_name'] == to:
                channel_name = item['channel_name']
                print(channel_name)
                break

        # 判断是否在已登录记录中
        if channel_name != '':
            # Send message to room
            #print(text_data_json)
            await self.channel_layer.send(
                channel_name,
                {
                    'type': 'chat_message',
                    'message': text_data_json,
                }
            )
            print("发送成功")
        else:
            # 否则，存入数据库
            await self.savemsg(text_data_json)
            print("恭喜！已存入数据库")

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket。发送到前端
        #print(message)
        await self.send(text_data=json.dumps({
            'message': [message]
        }))

    @database_sync_to_async
    def savemsg(self, text_data_json):
        print("save to database")
        From_name = text_data_json['from']
        To_name = text_data_json['to']
        Content = text_data_json['content']
        Time = text_data_json['time']
        Isread = text_data_json['isread']
        MSg = Tbquery.objects.create(From_name=str(From_name), To_name=str(To_name), q_content =str(Content), q_time=str(Time),Isread=int(Isread))
        MSg.save()

    # @database_sync_to_async
    # def send(self, text_data):
    #     print("send history data")
    #     channel_name = ''
    #     await self.channel_layer.send(
    #         channel_name,
    #         {
    #             'type': 'chat_message',
    #             'message': text_data,
    #         }
    #     )
    #     print("发送成功")

    @database_sync_to_async
    def readhistorymsg(self, From_name, To_name):
        Msg = Tbquery.objects.filter(From_name=From_name,To_name=To_name)
        return Msg

# class ChatGroupConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # 向组发送的
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#
#
#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         # 从在线列表中移除后退出
#         await self.close()
#
#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)['message']
#
#
#
#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']
#         # Send message to WebSocket。发送到前端
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

