from ResourceManager.NetworkManager import NetworkManager
from time import sleep

if __name__ == "__main__":
    networkManager = NetworkManager()
    networkManager.start()
    try:
        sleep(240)
    finally:
        networkManager.stop()