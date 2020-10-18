from CheckRouterStatus import CheckRouterStatus
from StartRouter import startRouter

def refreshNetwork():
    checkStatus = CheckRouterStatus()
    getStatus = checkStatus.checkRouters()
    for router in getStatus['DOWN']:
        startRouter(router)

if __name__ == "__main__":
    
    refreshNetwork()



