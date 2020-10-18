import os

ROUTERS = ["'[r]1.click'",
           "'[r]4.click'",
           "'[r]2.click'",
           "'[r]3.click'",
           "'[r]5.click'",
           "'[r]6.click'",
           "'[b]1.click'",
           "'[b]2.click'",
           "'[b]3.click'",
           "'[b]4.click'",
           "'[b]5.click'",
           "'[b]6.click'",
           "'[b]7.click'",
           "'[b]8.click'",
           "'[b]9.click'",
           "'[b]10.click'"]

class CheckRouterStatus:

    def __init__(self):
        self.STATUS = {
            'UP':[],
            'DOWN':[]
        }

    def getProcessID(self, processName):
        command  = "ps aux | grep " + processName + " | awk '{print $2}' > PID.txt"
        os.system(command)
        with open('PID.txt','r') as f:
            processID = f.readline()
        processID = processID.replace('\n','')

        os.system('rm -f PID.txt')
        return processID

    def checkRouters(self):
        for router in ROUTERS:
            processID = self.getProcessID(router)
            if len(processID)>1:
                name = router.replace('[','').replace(']','').strip("'")
                proc = name + '  PID:  ' + processID
                self.STATUS['UP'].append(proc)
            else:
                name = router.replace('[','').replace(']','').strip("'")
                self.STATUS['DOWN'].append(name)
        
        print('ROUTERS NOT UP ARE :'),
        print(self.STATUS['DOWN'])
        return self.STATUS

if __name__ == "__main__":
    checkStatus = CheckRouterStatus()
    checkStatus.checkRouters()
        
    