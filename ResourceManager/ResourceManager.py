import os


NODES = [[],
         [],
         [],
         [["'[b]1.click'", "'[b]4.click'"],["'[b]2.click'","'[b]5.click'"],["'[b]6.click'","'[b]7.click'"]],
         [["'[b]8.click'", "'[b]9.click'"]],
         [["'[b]10.click'","'[b]3.click'"]]]
class ResourceManager:

    def __init__(self, RMID):
        self.RM_NODES = NODES[RMID-1]


    def getProcessID(self, processName):
        command  = "ps aux | grep " + processName + " | awk '{print $2}' > PID.txt"
        os.system(command)
        with open('PID.txt','r') as f:
            processID = f.readline()
        os.system('rm -f PID.txt')
        return processID
    
    def killProcess(self, processName):
        processID = self.getProcessID(processName)
        command = 'kill '+ processID
        os.system(command)

    def updatePID(self):
        print(self.RM_NODES)
        return 0



if __name__ == "__main__":

    RM = ResourceManager(4)
    RM.killProcess(NODES[3][0][1])

