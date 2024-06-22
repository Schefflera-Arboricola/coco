import time
from coco.utils.backend import _dispatchable

__all__ = [
    "temper",
    "melt",
]


@_dispatchable
def temper(C):
    print("tempering...")
    t = C.cooling_time()
    C.temp = C.tempering_point
    time.sleep(t)
    print(f"tempering done in {t:.2f} seconds")


@_dispatchable
def melt(C):
    print("melting...")
    t = C.melting_time()
    C.temp = C.melting_point
    time.sleep(t)
    print(f"melting done in {t:.2f} seconds")
