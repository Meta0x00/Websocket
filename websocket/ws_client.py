#! -*- coding=utf-8 -*-
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8000") as ws:
        name = input("input: ")
        await ws.send(name)
        print(f"> {name}")
        recv = await ws.recv()
        print(f"> {recv}")

asyncio.get_event_loop().run_until_complete(hello())
