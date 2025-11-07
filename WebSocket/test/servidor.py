# servidor.py
import asyncio
import websockets

async def handler(websocket):
    print("Cliente conectado.")
    async for message in websocket:
        print(f"Mensaje recibido: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Servidor WebSocket escuchando en ws://localhost:8765")
        await asyncio.Future()  # se queda corriendo

asyncio.run(main())
