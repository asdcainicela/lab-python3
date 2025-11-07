import asyncio

async def tarea(nombre):
    print(f"{nombre} inicia")
    await asyncio.sleep(2)
    print(f"{nombre} termina")

async def main():
    tareas = [tarea("A"), tarea("B"), tarea("C")]
    await asyncio.gather(*tareas)

asyncio.run(main())
