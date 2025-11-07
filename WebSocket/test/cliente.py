# cliente.py
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hola servidor!")
        respuesta = await websocket.recv()
        print(f"Respuesta del servidor: {respuesta}")

asyncio.run(hello())
