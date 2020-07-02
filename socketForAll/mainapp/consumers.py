import json, asyncio, math, random, string, uuid
from channels.generic.websocket import AsyncWebsocketConsumer


class mainConsumer(AsyncWebsocketConsumer):

    def __init__(self, other):
        self.times = 0
        self.uuid = uuid.uuid4()
        super().__init__(other)

    async def connect(self):
        await self.accept()
        print("connection successful!")

    async def disconnect(self, close_code):
        allUsers.remove(self)
        print("connection closed! ")

    async def receive(self, text_data):
        allData = json.loads(text_data)
        await self.afterInit(allData)


    async def afterInit(self, message) :

        try:
            if message['geometry']:
                if message['geometry'] == 'circle':
                    while True:
                        await self.send(text_data = json.dumps({
                                'message': self.getCircle(message['center'], message['radius'], message['speed'])
                            })
                        )
                        await asyncio.sleep(1)
                elif message['geometry'] == 'rectangle':
                    pass
        except:
            pass

        try:
            if message['data_type']:
                if message['data_type'] == 'string':
                    while True:
                        await self.send(text_data = json.dumps({
                                'message': self.getString(message['length'])
                            })
                        )
                        await asyncio.sleep(1)

                elif message['data_type'] == 'integer':
                    print(message)
                    while True:
                        await self.send(text_data = json.dumps({
                                'message': self.getInteger(message['min'], message['max'])
                            })
                        )

                        await asyncio.sleep(1)
        except:
            pass


    def getString(self, length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def getInteger(self, min, max):
        return random.randrange(min, max)

    def getCircle(self, center, radius, inc):
        theta = self.times
        self.times += inc

        x = radius * math.cos(theta)  + center[0]
        y = radius * math.sin(theta) + center[1]

        return (x, y)
