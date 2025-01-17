import threading
from time import sleep
from time import time
import random
import logging


logging.basicConfig(level=logging.DEBUG)


# lock = threading.Semaphore(1)
lock = threading.Lock()
start = time()


def log(message: str):
    t = time() - start
    name = threading.current_thread().getName()
    logging.debug("[%6.3f] %s: %s", t, name, message)


def train(transit_time, arrive_time):
    sleep(arrive_time)
    log("arrived to the sector")
    # lock.acquire()
    with lock:
        log(f"starts passing the sector")
        sleep(transit_time)
    # lock.release()
    log("passed the sector")
    print(f"{threading.current_thread().getName()} passed the sector.")


if __name__ == "__main__":
    n = 10
    t1 = 1
    t2 = 5
    t3 = 0
    t4 = 30

    ths = []
    for i in range(n):
        transit_time = random.random() * (t2 - t1) + t1
        arrive_time = random.random() * (t4 - t3) + t3
        ths.append(
            threading.Thread(
                target=train,
                args=(transit_time, arrive_time),
                name=f"Train {i}"
            )
        )
        print(
            f"Train {i} arrives at {arrive_time:6.3f} "
            f"and passes for {transit_time:6.3f}"
        )

    for th in ths:
        th.start()
    for th in ths:
        th.join()
    log("all trains passed the sector")
