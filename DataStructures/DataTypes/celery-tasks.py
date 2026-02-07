# celery: aynsc task queue implementation
from __future__ import absolute_import
import os
from celery import Celery
from time import sleep

app = Celery('celery-tasks', broker='redis://localhost:6300', backend='redis://localhost:6300')
@app.task
def process(x, y):
    i= 0
    while i < 5:
        sleep(1)
        i += 1
        print(f"Processing {x} and {y}...")
    
    return x**2 + y**2

print(process(2,3))
#process.delay(2,3)

