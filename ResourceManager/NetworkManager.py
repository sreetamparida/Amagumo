from threading import Timer
from ResourceManager import ResourceManager
from Tools.RefreshNetwork import refreshNetwork
from random import randint
import string
from time import sleep

class NetworkManager:

    def __init__(self):
        self.manager = None
        self.isRunning = False
        self.interval = 120
        self.count = 0

    def _run(self):
        self.isRunning = False
        self.start()
        self._manageNetwork()
    
    def start(self):
        if not self.isRunning:
            self.manager = Timer(self.interval, self._run)
            self.manager.start()
            self.is_running = True

    def stop(self):
        self.manager.cancel()
        self.isRunning = False

    def _generateKeys(self):
        keys = list(string.ascii_lowercase)
        values = []
        for _ in range(5):
            values.append(keys[randint(0,25)])
        return values


    def _manageNetwork(self):
        if self.count < 5:
            self.count+=1
            rm = ResourceManager()
            refreshNetwork()
            RMID = [4,5,6]
            print('Starting to Update PIDS')
            for rmid in RMID:
                values = self._generateKeys()
                rm.updatePID(rmid, values)
            print('PID Updation Complete')

        

if __name__ == "__main__":
    networkManager = NetworkManager()
    networkManager.start()
    try:
        sleep(240)
    finally:
        networkManager.stop()