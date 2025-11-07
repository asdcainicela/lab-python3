import threading
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread


def sumar(a,b):
    time.sleep(0.1)
    thread = current_thread()
    print(f"{thread.name} sumando {a} + {b}")
    print(a+b, "\n")

executer = ThreadPoolExecutor(max_workers=2)
executer.submit(sumar, 1, 2)
executer.submit(sumar, 3, 4)
executer.submit(sumar, 5, 6)
executer.submit(sumar, 7, 8)
executer.submit(sumar, 9, 10) 