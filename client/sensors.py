import psutil
import requests
from threading import Thread

class A(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            self.a = psutil.cpu_freq().current
            self.b = psutil.virtual_memory().percent
            task = {"cpu_freq":self.a,  "ram_usage":self.b}
            resp = requests.post('http://192.168.1.101:8000/sensorA/', json=task)

            if resp.status_code != 201:
                print("error")

A()
while True:
    pass