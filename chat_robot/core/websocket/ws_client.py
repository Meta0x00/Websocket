#! -*- coding=utf-8 -*-
import asyncio
import websockets

class WsClient(object):
    def __init__(self):
        self.port = 7001
        self.host = "localhost"
    async def client_run(self):
        async with websockets.connect(f"ws://{self.host}:{self.port}") as ws:
            msg = input("Input: ")
            print(f"> Send {msg}")
            await ws.send(msg)
            recv = await ws.recv()
            print(f"< From server {recv}")

asyncio.get_event_loop().run_until_complete(WsClient().client_run())
