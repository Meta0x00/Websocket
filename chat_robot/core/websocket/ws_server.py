#! -*- coding=utf-8 -*-
import asyncio
import websockets
from conf import websocket_conf

class WsServer(object):
    def __init__(self):
        self.port = websocket_conf.port
        self.host = websocket_conf.host

    async def server(self, websocket, path):
        while True:
            msg = await websocket.recv()
            print(f"> From client {msg}")
            await websocket.send(msg)

    def server_run(self):
        asyncio.get_event_loop().run_until_complete(websockets.serve(self.server, str(self.host), int(self.port)))
        asyncio.get_event_loop().run_forever()
